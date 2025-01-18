from type_form.interactors.storage_interfaces.storage_interface import StorageInterface, TabDTO, SectionConfigDTO
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.exceptions import custom_exceptions

class FormLayoutInteractor:

    def __init__(self, storage:StorageInterface):

        self.storage = storage

    def create_layout_for_form_wrapper(self, user_id:str, form_id:int, layout_name:str, presenter:PresenterInterface):
        """ELP
            check if user exists
            check if form exists
            check if layout already exists for form
            create layout for form
        """

        try:
            layout_id = self.create_layout_for_form(user_id=user_id, form_id=form_id, layout_name=layout_name)
        except custom_exceptions.InvalidUserException:
            presenter.raise_exception_for_invalid_user()
        except custom_exceptions.InvalidFormException:
            presenter.raise_exception_for_invalid_form()
        except custom_exceptions.LayoutAlreadyExistsException:
            presenter.raise_exception_for_layout_already_exists()
        else:
            return presenter.get_response_for_create_layout_for_form(id=layout_id)
    
    def create_layout_for_form(self, user_id:str, form_id:int, layout_name:str):

        self._check_if_input_data_is_correct(user_id=user_id, form_id=form_id)

        return self.storage.create_layout_for_form(user_id=user_id, form_id=form_id, layout_name=layout_name)
    
    def _check_if_input_data_is_correct(self, user_id:str, form_id:int):

        self.storage.check_user(id=user_id)

        self.storage.check_form(id=form_id)

        self.storage.check_if_layout_already_exists_for_form(form_id=form_id)

    
    def create_tab_for_layout_for_section_config_wrapper(self, tab_dto:TabDTO, presenter:PresenterInterface):
        """ELP
            check if user exists
            check if layout exists
            check if tab already exists for layout
            create tab for layout
        """
        try:
            tab_id = self.create_tab_for_layout(tab_dto=tab_dto)
        except custom_exceptions.InvalidUserException:
            presenter.raise_exception_for_invalid_user()
        except custom_exceptions.InvalidLayoutException:
            presenter.raise_exception_for_invalid_layout()
        except custom_exceptions.TabAlreadyExistsException:
            presenter.raise_exception_for_tab_already_exists()
        else:
            return presenter.get_response_for_create_tab_for_layout(id=tab_id)
    
    def create_tab_for_layout_for_section_config(self, tab_dto:TabDTO):
        
        self._check_if_input_data_is_correct_for_create_tab_for_layout_for_section_config(tab_dto=tab_dto)

        return self.storage.create_tab_for_layout_for_section_config(tab_dto=tab_dto)

    def _check_if_input_data_is_correct_for_create_tab_for_layout_for_section_config(self, tab_dto:TabDTO):

        self.storage.check_user(id=tab_dto.user_id)

        self.storage.check_layout(id=tab_dto.layout_id)

        self.storage.check_if_tab_already_exists_for_layout(layout_id=tab_dto.layout_id, tab_type=tab_dto.tab_type)
    
    def add_section_to_tab(self, tab_id:int, sectionconfig_dtos:list[SectionConfigDTO]):

        self.storage.check_tab(id=tab_id)

        return self.storage.add_sections_to_tab(tab_id=tab_id, sectionconfig_dtos=sectionconfig_dtos)
    
    def get_tab_details_wrapper(self, tab_id:int, presenter:PresenterInterface):
        """ELP
            check if tab exists
            get tab details
        """
        try:
            tab_dto = self.get_tab_details(tab_id=tab_id)
        except custom_exceptions.InvalidTabException:
            presenter.raise_exception_for_invalid_tab()
        else:
            return presenter.get_response_for_tab_details(tab_dto=tab_dto)

    def get_tab_details(self, tab_id:int):

        self.storage.check_tab(id=tab_id)

        return self.storage.get_tab_details(tab_id=tab_id)