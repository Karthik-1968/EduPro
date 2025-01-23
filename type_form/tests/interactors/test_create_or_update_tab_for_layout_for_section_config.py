from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions import custom_exceptions
from type_form.interactors.form_layout_interactor import FormLayoutInteractor
from faker import Faker
import factory
from type_form.models import Tab
import pytest
from mock import create_autospec
from type_form.interactors.storage_interfaces.storage_interface import TabDTO

fake = Faker()

class TabFactory(factory.Factory):
    class Meta:
        model = Tab
    user_id = fake.uuid4()
    layout_id = fake.random_int()
    tab_type = fake.word()
    tab_name = fake.word()

class TestCreateOrUpdateTabForLayoutForSectionConfig:

    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.interactor = FormLayoutInteractor(storage=self.storage)

    def test_if_user_id_does_not_exist_raises_exception(self):
        tab_factory = TabFactory()
        tab_id = 1
        tab_dto = TabDTO(tab_id=tab_id, user_id=tab_factory.user_id, layout_id=tab_factory.layout_id, tab_type=\
                                                    tab_factory.tab_type, tab_name=tab_factory.tab_name)
        self.storage.check_user.side_effect = custom_exceptions.InvalidUserException
        with pytest.raises(custom_exceptions.InvalidUserException):
            self.interactor.create_or_update_tab_for_layout_for_section_config(tab_dto)
        
        self.storage.check_user.assert_called_once_with(id=tab_dto.user_id)

    def test_if_layout_id_does_not_exist_raises_exception(self):
        tab_factory = TabFactory()
        tab_id = 1
        tab_dto = TabDTO(tab_id=tab_id, user_id=tab_factory.user_id, layout_id=tab_factory.layout_id, tab_type=\
                                                    tab_factory.tab_type, tab_name=tab_factory.tab_name)
        self.storage.check_layout.side_effect = custom_exceptions.InvalidLayoutException(layout_id=tab_dto.layout_id)
        with pytest.raises(custom_exceptions.InvalidLayoutException):
            self.interactor.create_or_update_tab_for_layout_for_section_config(tab_dto)
        
        self.storage.check_layout.assert_called_once_with(id=tab_dto.layout_id)

    def test_if_tab_already_exists_for_layout_raises_exception(self):
        tab_factory = TabFactory()
        tab_id = 1
        tab_dto = TabDTO(tab_id=tab_id, user_id=tab_factory.user_id, layout_id=tab_factory.layout_id, tab_type=\
                                                    tab_factory.tab_type, tab_name=tab_factory.tab_name)
        self.storage.check_if_tab_already_exists_for_layout.side_effect = custom_exceptions.TabAlreadyExistsException(layout_id=tab_dto.layout_id, \
                                                                                                        tab_type=tab_dto.tab_type)
        with pytest.raises(custom_exceptions.TabAlreadyExistsException):
            self.interactor.create_or_update_tab_for_layout_for_section_config(tab_dto)
        
        self.storage.check_if_tab_already_exists_for_layout.assert_called_once_with(layout_id=tab_dto.layout_id, tab_type=tab_dto.tab_type)

    def test_create_or_update_tab_for_layout_for_section_config(self):

        tab_factory = TabFactory()
        tab_id = 1
        tab_dto = TabDTO(tab_id=tab_id, user_id=tab_factory.user_id, layout_id=tab_factory.layout_id, tab_type=\
                                                    tab_factory.tab_type, tab_name=tab_factory.tab_name)

        expected_output = tab_id
        self.storage.create_or_update_tab_for_layout_for_section_config.return_value = expected_output
        actual_output = self.interactor.create_or_update_tab_for_layout_for_section_config(tab_dto)

        assert actual_output == expected_output

        self.storage.check_user.assert_called_once_with(id=tab_dto.user_id)
        self.storage.check_layout.assert_called_once_with(id=tab_dto.layout_id)
        self.storage.check_if_tab_already_exists_for_layout.assert_called_once_with(layout_id=tab_dto.layout_id, tab_type=tab_dto.tab_type)
        self.storage.create_or_update_tab_for_layout_for_section_config.assert_called_once_with(tab_dto=tab_dto)
