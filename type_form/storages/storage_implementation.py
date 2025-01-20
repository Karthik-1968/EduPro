from type_form.exceptions.custom_exceptions import UserAlreadyPresentException, InvalidUserException, WorkspaceAlreadyExistsException,\
    InvalidWorkspaceException, AlreadyInvitedException, InvalidInvitationException, AlreadyAcceptedException,\
        FormAlreadyExistsException, InvalidFormException, FieldAlreadyExistsException, InvalidFieldException,\
            MaximumInvitesLimitReachedException, SettingsAlreadyExistsException, InvalidFormFieldException,\
                InvalidSettingsException, InvitationExpiredException, LayoutAlreadyExistsException, InvalidLayoutException,\
                    TabAlreadyExistsException, InvalidTabException, InvalidLayoutForFormException
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.models import User, Workspace, Form, Field, FormResponse, FormField, FormFieldResponse, FormFieldSettings,\
    WorkspaceInvite, Layout, Tab
from type_form.interactors.storage_interfaces.storage_interface import UserDTO, WorkspaceDTO, FormDTO, FieldDTO, FormFieldDTO, \
    FormResponseDTO, FormFieldResponseDTO, WorkspaceInviteDTO, PhoneNumberFieldSettingsDTO, SectionConfigDTO, TabDTO
from datetime import datetime
from json import loads, dumps

class StorageImplementation(StorageInterface):
    
    def check_if_user_already_present(self, email: str):
        
        if User.objects.filter(email = email).exists():
            raise UserAlreadyPresentException
        
    def create_user(self, id: str, email: str)->str:
        User.object.create(id = id, email = email)
        
        return email
    
    def check_user(self, id: str):
        
        user_exists = User.objects.filter(id = id).exists()
        user_not_exists = not user_exists
        if user_not_exists:
            raise InvalidUserException
        
    def check_if_workspace_already_exists(self, name: str):
        
        if Workspace.objects.filter(name = name).exists():
            raise WorkspaceAlreadyExistsException
        
    def create_workspace(self, user_id: str, name: str, is_private: bool, max_invites: int)->int:
        
        workspace = Workspace.objects.create(user_id = user_id, name = name, is_private = is_private, max_invites = max_invites)
        
        return workspace.id
    
    def get_workspaces_of_user(self, id:str)->list[WorkspaceDTO]:
        
        workspaces = Workspace.objects.filter(user_id = id)
        workspacedtos = []
        for workspace in workspaces:
            workspacedto = self.convert_workspace_object_to_dto(workspace)
            workspacedtos.append(workspacedto)
        
        return workspacedtos
    
    def convert_workspace_objects_to_dtos(workspace):
        
        return WorkspaceDTO(
            user_id = workspace.user_id,
            name = workspace.name,
            is_private = workspace.is_private,
            max_invites = workspace.max_invites
        )
    
    def check_workspace(self, id: int):
        workspace_exists = Workspace.objects.filter(id = id).exists()
        workspace_not_exists = not workspace_exists
        if workspace_not_exists:
            raise InvalidWorkspaceException
        
    def check_if_user_already_invited(self, user_id: str, workspace_id: int):
        if WorkspaceInvite.objects.filter(user_id = user_id, workspace_id = workspace_id).exists():
            raise AlreadyInvitedException
        
    def check_if_invites_limit_reached(self, id:int):
        workspace = Workspace.objects.get(id = id)
        if workspace.max_invities == workspace.invites_sent:
            raise MaximumInvitesLimitReachedException
        
    def create_workspace_invite(self, name:str, user_id:str, workspace_id:int, role:int, is_accepted:bool, expiry_time:str):
        
        workspace_invite = WorkspaceInvite.objects.create(name = name, user_id = user_id, workspace_id = workspace_id, role = role,\
            is_accepted = is_accepted, expiry_time = expiry_time)
        
        workspace = Workspace.objects.get(id = workspace_id)
        workspace.invites_sent += 1
        
        return workspace_invite.id
    
    def check_workspace_invite(self, id:int):
        
        workspace_invite_exists = WorkspaceInvite.objects.filter(id = id).exists()
        workspace_invite_not_exists = not workspace_invite_exists
        if workspace_invite_not_exists:
            raise InvalidInvitationException
        
    def check_if_invitation_already_accepted(self, id:int):
        
        workspace_invite = WorkspaceInvite.objects.get(id = id)
        if workspace_invite.is_accepted:
            raise AlreadyAcceptedException
        
    def check_if_invitation_expired(self, id):
        
        workspace_invite = WorkspaceInvite.objects.get(id = id)
        if workspace_invite.expiry_time < datetime.now():
            raise InvitationExpiredException
        
    def accept_invitation(self, id:int):
        
        workspace_invite = WorkspaceInvite.objects.get(id = id)
        workspace_invite.is_accepted = True
        workspace_invite.save()
        
    def reject_invitation(self, id:int):
        
        workspace_invite = WorkspaceInvite.objects.get(id = id)
        workspace_invite.delete()
        
    def get_invities_of_workspace(self, id:int)->list[WorkspaceInviteDTO]:
        
        workspace_invites = WorkspaceInvite.objects.filter(workspace_id = id)
        workspaceinvitedtos = []
        for workspace_invite in workspace_invites:
            workspaceinvitedto = self.convert_workspace_invite_object_to_dto(workspace_invite)
            workspaceinvitedtos.append(workspaceinvitedto)
        
        return workspaceinvitedtos
    
    def convert_workspace_invite_object_to_dto(self, workspace_invite):
        
        return WorkspaceInviteDTO(
            name = workspace_invite.name,
            user_id = workspace_invite.user_id,
            workspace_id = workspace_invite.workspace_id,
            role = workspace_invite.role,
            is_accepted = workspace_invite.is_accepted,
            expiry_time = workspace_invite.expiry_time
        )
        
    def check_if_form_already_exists(self, name:str):
        
        if Form.objects.filter(name = name).exists():
            raise FormAlreadyExistsException
        
    def create_form(self, user_id:str, workspace_id:int, name:str)->int:
        
        form = Form.objects.create(user_id = user_id, workspace_id = workspace_id, name = name)
        
        return form.id
    
    def get_forms_of_workspace(self, id:int)->list[FormDTO]:
        
        forms = Form.objects.filter(workspace_id = id)
        formdtos = []
        for form in forms:
            formdto = self.convert_form_object_to_dto(form)
            formdtos.append(formdto)
        
        return formdtos
    
    def convert_form_object_to_dto(form):
        
        return FormDTO(
            user_id = form.user_id,
            workspace_id = form.workspace_id,
            name = form.name
        )
        
    def get_forms_of_user(self, id:str)->list[FormDTO]:
        
        forms = Form.objects.filter(user_id = id)
        formdtos = []
        for form in forms:
            formdto = self.convert_form_object_to_dto(form)
            formdtos.append(formdto)
        
        return formdtos
        
    def check_if_field_already_exists(self, field_type:str):
        
        if Field.objects.filter(field_type = field_type).exists():
            raise FieldAlreadyExistsException
        
    def create_field(self, field_name:str, field_type:str)->int:
        
        field = Field.objects.create(field_name = field_name, field_type = field_type)
        
        return field.id
    
    def check_form(self, id:int):
        
        form_exists = Form.objects.filter(id = id).exists()
        form_not_exists = not form_exists
        if form_not_exists:
            raise InvalidFormException(form_id=id)
        
    def check_field(self, id:int):
        
        field_exists = Field.objects.filter(id = id).exists()
        field_not_exists = not field_exists
        if field_not_exists:
            raise InvalidFieldException
    
    def add_field_to_form(self, form_id:int, user_id:str, field_id:int,setting_id:int, is_required:bool, label_text:str, \
        label_vedio:str, group_name:str)->int:
        
        form_field = FormField.objects.create(form_id = form_id, user_id = user_id, field_id = field_id, setting_id = setting_id,\
            is_required = is_required, label_text = label_text, label_vedio = label_vedio, group_name = group_name)
        
        return form_field.id
    
    def get_fields_of_form(self, id:int)->list[FormFieldDTO]:
        
        form_fields = FormField.objects.filter(form_id = id)
        formfielddtos = []
        for form_field in form_fields:
            formfielddto = self.convert_form_field_object_to_dto(form_field)
            formfielddtos.append(formfielddto)
        
        return formfielddtos
    
    def convert_form_field_object_to_dto(form_field):
        
        return FormFieldDTO(
            form_id = form_field.form_id,
            user_id = form_field.user_id,
            field_id = form_field.field_id,
            settings_id = form_field.setting_id,
            is_required = form_field.is_required,
            label_text = form_field.label_text,
            label_vedio = form_field.label_vedio,
            group_name = form_field.group_name
        )
        
    def create_form_response(self, user_id:str, data:str, form_id:int, device:str, status:str, form_field_data:str):
        
        form_response = FormResponse.objects.create(user_id = user_id, form_id = form_id, data = data, device = device, \
            status = status)
        
        form = Form.objects.get(id = form_id)
        if status == "submitted":
            form.submissions_count += 1
            form.save()
        elif status == "in progress":
            form.views_count += 1
            form.save()
            
        completion_rate = (form.submissions_count / form.views_count) * 100
        form.completion_rate = completion_rate
        form.save()
        
        for form_field_id, form_field_value in form_field_data.items():
            FormFieldResponse.objects.create(form_response_id = form_response.id, form_field_id = form_field_id,\
                value = form_field_value)
        
        return form_response.id
    
    def get_responses_of_form(self, id:int)->list[FormResponseDTO]:
        
        form_responses = FormResponse.objects.filter(form_id = id)
        formresponsedtos = []
        for form_response in form_responses:
            formresponsedto = self.convert_form_response_object_to_dto(form_response)
            formresponsedtos.append(formresponsedto)
        
        return formresponsedtos
    
    def convert_form_response_object_to_dto(form_response):
        
        return FormResponseDTO(
            user_id = form_response.user_id,
            form_id = form_response.form_id,
            data = form_response.data,
            device = form_response.device,
            status = form_response.status
        )
        
    def get_responses_of_user(self, id:int)->list[FormResponseDTO]:
        
        form_responses = FormResponse.objects.filter(user_id = id)
        formresponsedtos = []
        for form_response in form_responses:
            formresponsedto = self.convert_form_response_object_to_dto(form_response)
            formresponsedtos.append(formresponsedto)
        
        return formresponsedtos
    
    def check_if_settings_exists(self, multiple_selection:bool, multiple_selection_scope:list[str], choices:list[str],\
        phone_number_choices:list[PhoneNumberFieldSettingsDTO], max_number:int, min_number:int, max_length:int, min_length:int,\
            other_option:bool, vetical_alignment:bool, alphabetical_order:bool, placeholder:str):
        
        if FormFieldSettings.objects.filter(multiple_selection = multiple_selection,\
            multiple_selection_scope = multiple_selection_scope, choices = choices, phone_number_choices = phone_number_choices,\
                max_number = max_number, min_number = min_number, max_length = max_length, min_length = min_length,\
                    other_option = other_option, vetical_alignment = vetical_alignment, alphabetical_order = alphabetical_order,\
                        placeholder = placeholder).exists():
            
            raise SettingsAlreadyExistsException
        
    def create_settings(self, multiple_selection:bool, multiple_selection_scope:list[str], choices:list[str],\
        phone_number_choices:list[PhoneNumberFieldSettingsDTO], max_number:int, min_number:int, max_length:int, min_length:int,\
            other_option:bool, vetical_alignment:bool, alphabetical_order:bool, placeholder:str):
        
        settings = FormFieldSettings.objects.create(multiple_selection = multiple_selection, multiple_selection_scope = multiple_selection_scope,\
            choices = choices, phone_number_choices = phone_number_choices, max_number = max_number, min_number = min_number,\
                max_length = max_length, min_length = min_length, other_option = other_option, vetical_alignment = vetical_alignment,\
                    alphabetical_order = alphabetical_order, placeholder = placeholder)
        
        return settings.id
    
    def check_form_field(self, form_field_id:int):
        
        form_field_exists = FormField.objects.filter(id = form_field_id).exists()
        form_field_not_exists = not form_field_exists
        if form_field_not_exists:
            raise InvalidFormFieldException
        
    def check_settings(self, settings_id:int):
        
        settings_exists = FormFieldSettings.objects.filter(id = settings_id).exists()
        settings_not_exists = not settings_exists
        if settings_not_exists:
            raise InvalidSettingsException
    
    def add_settings_to_form_field(self, form_field_id:int, settings_id:int):
        
        form_field = FormField.objects.get(id = form_field_id)
        form_field.settings_id = settings_id
        form_field.save()
        
    def get_submissions_count_of_form(self, id:int)->int:
        
        form = Form.objects.get(id = id)
        
        return form.submissions_count
    
    def get_views_count_of_form(self, id:int)->int:
        
        form = Form.objects.get(id = id)
        
        return form.views_count
    
    def get_form_completion_rate(self, id:int)->float:
        
        form = Form.objects.get(id = id)
        
        return form.completion_rate

    def check_if_layout_is_valid_for_form(self, form_id:int, layout_id:int):
        
        if Layout.objects.filter(form_id = form_id).exists():
            layout = Layout.objects.get(form_id = form_id)

            if layout.id!=layout_id:
                raise InvalidLayoutForFormException(form_id=form_id, layout_id=layout_id)


    def create_or_update_layout_for_form(self, user_id:str, form_id:int, layout_name:str, layout_id:int)->int:

        if Layout.objects.filter(form_id = form_id).exists():
            layout = Layout.objects.get(form_id = form_id)

            layout.layout_name = layout_name
            layout.save()

            return layout.id
        else:
            layout = Layout.objects.create(id=layout_id, user_id = user_id, form_id = form_id, layout_name = layout_name)

            return layout.id

    def check_layout(self, id:int):
        
        layout_exists = Layout.objects.filter(id = id).exists()
        layout_not_exists = not layout_exists
        if layout_not_exists:
            raise InvalidLayoutException(layout_id=id)

    def create_or_update_tab_for_layout_for_section_config(self, tab_dto:TabDTO)->int:

        if Tab.objects.filter(layout_id = tab_dto.layout_id, id=tab_dto.tab_id).exists():
            tab = Tab.objects.get(layout_id = tab_dto.layout_id, id=tab_dto.tab_id)

            tab.tab_name = tab_dto.tab_name
            tab.save()

            return tab.id
        else:
            config = {
                "sections_config": []
            }

            config = dumps(config)

            tab = Tab.objects.create(user_id = tab_dto.user_id, layout_id = tab_dto.layout_id, tab_type = tab_dto.tab_type, \
                                    tab_name = tab_dto.tab_name, config = config)

            return tab.id

    def check_if_form_fields_exists(self, form_fields:list[str]):

        for form_field_id in form_fields:
            form_field_exists = FormField.objects.filter(id = form_field_id).exists()
            form_field_not_exists = not form_field_exists
            if form_field_not_exists:
                raise InvalidFormFieldException

    def check_if_form_fields_belong_to_form(self, form_fields:list[str], layout_id:int):

        form_id = Layout.objects.get(id = layout_id).form_id
        for form_field_id in form_fields:
            form_field = FormField.objects.get(id = form_field_id)
            if form_field.form_id != form_id:
                raise FieldDoesNotBelongToFormException

    def check_tab(self, id:int):
        
        tab_exists = Tab.objects.filter(id = id).exists()
        tab_not_exists = not tab_exists
        if tab_not_exists:
            raise InvalidTabException

    def get_tab_details(self, tab_id:int)->TabDTO:

        tab = Tab.objects.get(id = tab_id)
        tab_dto = self.convert_tab_object_to_dto(tab)

        return tab_dto

    def convert_tab_object_to_dto(tab):
        
        return TabDTO(
            user_id = tab.user_id,
            layout_id = tab.layout_id,
            tab_type = tab.tab_type,
            tab_name = tab.tab_name
        )

    def add_section_to_tab(self, tab_id:int, sectionconfig_dto:SectionConfigDTO):

        tab = Tab.objects.get(id = tab_id)

        config = loads(tab.config)

        if sectionconfig_dto.section_type == "gof_name":
            config["sections_config"].append({
                "type": sectionconfig_dto.section_type,
                "gof_name": sectionconfig_dto.gof
            })

        elif sectionconfig_dto.section_type == "form_field ids":
            config["sections_config"].append({
                "section_name": sectionconfig_dto.section_name,
                "type": sectionconfig_dto.section_type,
                "formfield_ids": sectionconfig_dto.formfields
            })

        tab.config = dumps(config)
        tab.save()

    def update_layout_for_form(self, layout_id:int, layout_name:str):

        layout = Layout.objects.get(id = layout_id)
        layout.layout_name = layout_name
        layout.save()

    def update_tab_for_section_config(self, tab_id:int, tab_name:str):
        
        tab = Tab.objects.get(id = tab_id)
        tab.tab_name = tab_name
        tab.save()