from type_form.interactors.storage_interfaces.storage_interface import StorageInterface, TabDTO, SectionConfigDTO, FormFieldIdsConfigDTO
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.exceptions import custom_exceptions

class FormLayoutInteractor:

    def __init__(self, storage:StorageInterface):

        self.storage = storage

    def create_or_update_layout_for_form_wrapper(self, user_id:str, form_id:int, layout_name:str, presenter:PresenterInterface):
        """ELP
            check if user exists
            check if form exists
            check if layout already exists for form
            create layout for form
        """
        try:
            layout_id = self.create_or_update_layout_for_form(user_id=user_id, form_id=form_id, layout_name=layout_name)
        except custom_exceptions.InvalidUserException:
            presenter.raise_exception_for_invalid_user()
        except custom_exceptions.InvalidFormException:
            presenter.raise_exception_for_invalid_form()
        except custom_exceptions.LayoutAlreadyExistsException:
            presenter.raise_exception_for_layout_already_exists()
        else:
            return presenter.get_response_for_create_layout_for_form(id=layout_id)
    
    def create_or_update_layout_for_form(self, user_id:str, form_id:int, layout_name:str, layout_id:int):

        self._check_if_input_data_is_correct_for_create_or_update_layout_for_form(user_id=user_id, form_id=form_id, layout_id=layout_id)

        return self.storage.create_or_update_layout_for_form(user_id=user_id, form_id=form_id, layout_name=layout_name, layout_id=\
                                                                                                                layout_id)
    
    def _check_if_input_data_is_correct_for_create_or_update_layout_for_form(self, user_id:str, form_id:int, layout_id:int):

        self.storage.check_user(id=user_id)

        self.storage.check_form(id=form_id)

        self.storage.check_if_layout_is_valid_for_form(form_id=form_id, layout_id=layout_id)

    
    def create_tab_for_layout_for_section_config_wrapper(self, tab_dto:TabDTO, presenter:PresenterInterface):
        """ELP
            check if user exists
            check if layout exists
            check if tab already exists for layout
            create tab for layout
        """
        try:
            tab_id = self.create_or_update_tab_for_layout_for_section_config(tab_dto=tab_dto)
        except custom_exceptions.InvalidUserException:
            presenter.raise_exception_for_invalid_user()
        except custom_exceptions.InvalidLayoutException:
            presenter.raise_exception_for_invalid_layout()
        except custom_exceptions.TabAlreadyExistsException:
            presenter.raise_exception_for_tab_already_exists()
        else:
            return presenter.get_response_for_create_tab_for_layout(id=tab_id)
    
    def create_or_update_tab_for_layout_for_section_config(self, tab_dto:TabDTO):
        
        self._check_if_input_data_is_correct_for_create_or_update_tab_for_layout_for_section_config(tab_dto=tab_dto)

        return self.storage.create_or_update_tab_for_layout_for_section_config(tab_dto=tab_dto)

    def _check_if_input_data_is_correct_for_create_or_update_tab_for_layout_for_section_config(self, tab_dto:TabDTO):

        self.storage.check_user(id=tab_dto.user_id)

        self.storage.check_layout(id=tab_dto.layout_id)

    
    def add_section_to_tab(self, tab_id:int, sectionconfig_dto:SectionConfigDTO):
        """ELP:
                -check if tab exists
                -check if group name exists
                -check if form field ids exists
                -add section to tab
        """
        self.storage.check_tab(id=tab_id)

        if sectionconfig.section_type = "group_name":
            self.storage.check_group_name_exists_for_section_config(group_name=sectionconfig_dto.gof)

        if sectionconfig.section_type = "form_field_ids":
            self.storage.check_form_field_ids_exists_for_section_config(form_field_ids=sectionconfig_dto.formfields)

        return self.storage.add_section_to_tab(tab_id=tab_id, sectionconfig_dto=sectionconfig_dto)
    
    def create_or_update_tab_for_form_field_ids_config(self, tab_dto:TabDTO):       

        """ELP:
                -check if user exists
                -check if layout exists
                -create tab for list of form fields
        """
        self.storage.check_user(id=tab_dto.user_id)
        
        self.storage.check_layout(id=tab_dto.layout_id)

        return self.storage.create_or_update_tab_for_form_field_ids_config(tab_dto=tab_dto)

    
    def add_form_field_ids_to_tab(self, tab_id:int, form_field_ids_config_dto:FormFieldIdsConfigDTO):
        """ELP:
            -check if tab exists
            -check if form field ids exists
            -add form field ids to tab
        """
        self.storage.check_tab(id=tab_id)

        self.storage.check_form_field_ids_exists_for_form_field_ids_config(form_field_ids_config_dto=form_field_ids_config_dto)

        return self.storage.add_form_field_ids_to_tab(tab_id=tab_id, form_field_ids_config_dto=form_field_ids_config_dto)
    
    def get_layout_details_wrapper(self, layout_id:int):
        """ELP:
            -check if layout exists
            -get layout details
        """
        try:
            layout_details_dto = self.get_layout_details(layout_id=layout_id)
        except custom_exceptions.InvalidLayoutException:
            presenter.raise_exception_for_invalid_layout()
        else:
            return presenter.get_response_for_get_layout_details(layout_details_dto=layout_details_dto)

    def get_layout_details(self, layout_id:int):

        self.storage.check_layout(id=layout_id)

        return self.storage.get_layout_details(layout_id=layout_id)

    def add_child_tabs_to_parent_tab(self, parent_tab_id:int, child_tab_ids:list[int]):
        """ELP:
            -check if parent tab exists
            -check if child tabs exists
            -check if child tab is parent
            -add child tabs to parent tab
        """
        self.storage.check_tab(id=parent_tab_id)

        self.storage.check_tabs_exist(id = child_tab_ids)

        self.storage.check_if_child_tab_is_parent(child_tab_ids=child_tab_ids)

        return self.storage.add_child_tabs_to_parent_tab(parent_tab_id=parent_tab_id, child_tab_ids=child_tab_ids)