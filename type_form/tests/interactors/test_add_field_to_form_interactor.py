import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.field_interactor import FieldInteractor
from type_form.exceptions.custom_exceptions import InvalidFormException,InvalidUserException,InvalidFieldException

class TestAddFieldToFormInteractor:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = FieldInteractor(storage = self.storage, presenter = self.presenter)
        
    def test_given_invalid_form_id_raises_exception(self):
        
        form_id = 1
        field_id = 1
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        label_text = "My field"
        label_vedio = None
        is_required = True
        group_name = "Contact_details"
        setting_id = None
        
        self.storage.check_form.side_effect = InvalidFormException
        self.presenter.raise_exception_for_invalid_form.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.add_field_to_form(form_id = form_id, field_id = field_id, user_id = user_id, group_name = group_name,\
                label_text = label_text, label_vedio = label_vedio, is_required = is_required, setting_id = setting_id)
            
        self.storage.check_form.assert_called_once_with(id = form_id)
        self.presenter.raise_exception_for_invalid_form.assert_called_once()
        
    def test_given_invalid_user_id_raises_exception(self):
        
        form_id = 1
        field_id = 1
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        label_text = "My field"
        label_vedio = None
        is_required = True
        group_name = "Contact_details"
        setting_id = None
        
        self.storage.check_user.side_effect = InvalidUserException
        self.presenter.raise_exception_for_invalid_user.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.add_field_to_form(form_id = form_id, field_id = field_id, user_id = user_id, group_name = group_name,\
                label_text = label_text, label_vedio = label_vedio, is_required = is_required, setting_id = setting_id)
            
        self.storage.check_user.assert_called_once_with(id = user_id)
        self.presenter.raise_exception_for_invalid_user.assert_called_once()
        
    def test_given_invalid_field_id_raises_exception(self):
        
        form_id = 1
        field_id = 1
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        label_text = "My field"
        label_vedio = None
        is_required = True
        group_name = "Contact_details"
        setting_id = None
        
        self.storage.check_field.side_effect = InvalidFieldException
        self.presenter.raise_exception_for_invalid_field.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.add_field_to_form(form_id = form_id, field_id = field_id, user_id = user_id, group_name = group_name,\
                label_text = label_text, label_vedio = label_vedio, is_required = is_required, setting_id = setting_id)
            
        self.storage.check_field.assert_called_once_with(id = field_id)
        self.presenter.raise_exception_for_invalid_field.assert_called_once()
        
    def test_add_field_to_form(self):
        
        form_id = 1
        field_id = 1
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        label_text = "My field"
        label_vedio = None
        is_required = True
        group_name = "Contact_details"
        setting_id = None
        
        expected_form_field_id = 1
        expected_output= {
            "form_field_id": expected_form_field_id
        }
        
        self.storage.add_field_to_form.return_value = expected_form_field_id
        self.presenter.get_response_for_add_field_to_form.return_value = expected_output
        
        actual_output = self.interactor.add_field_to_form(form_id = form_id, field_id = field_id, user_id = user_id, \
            group_name = group_name, label_text = label_text, label_vedio = label_vedio, is_required = is_required, \
                setting_id = setting_id)
        
        assert actual_output == expected_output
        
        self.storage.add_field_to_form.assert_called_once_with(form_id = form_id, field_id = field_id, group_name = group_name,
            user_id = user_id, label_text = label_text, label_vedio = label_vedio, is_required = is_required, setting_id = setting_id)
        self.presenter.get_response_for_add_field_to_form.assert_called_once_with(id = expected_form_field_id)