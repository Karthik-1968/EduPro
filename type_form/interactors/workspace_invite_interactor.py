from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.storage_interfaces.storage_interface import WorkspaceInvitedto
import uuid
from type_form.exceptions.custom_exceptions import InvalidUser,MissingId,InvalidWorkspace,MissingRole,AlreadyAccepted,\
InvalidInvitation,AlreadyInvited

class WorkspaceInviteInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    def create_workspace_invite(self,user_id:uuid,workspace_id:int,is_accepted:bool,role:str):

        """
            ELP:
                check if input data exists
                check if user exists
                check if workspace exists
                check if already invited
                create workspace invite
        """
        
        self.validate_input_data_for_create_workspace_invite(user_id = user_id,workspace_id = workspace_id,role = role)

        try:
            self.storage.check_user(id = user_id)
        except InvalidUser:
            self.presenter.raise_exception_for_invalid_user()

        try:
            self.storage.check_workspace(id = workspace_id)
        except InvalidWorkspace:
            self.presenter.raise_exception_for_invalid_workspace()

        try:
            self.storage.check_if_user_already_invited(user_id = user_id,workspace_id = workspace_id)
        except AlreadyInvited:
            self.presenter.raise_exception_for_user_already_invited()

        userdto = self.storage.get_user(id = user_id)
        workspacedto = self.storage.get_workspace(id = workspace_id)

        workspaceinvitedto = WorkspaceInvitedto(user = userdto,workspace = workspacedto,role = role,is_accepted = is_accepted)

        workspace_id = self.storage.create_workspace_invite(workspacedinviteto = workspaceinvitedto)

        return self.presenter.get_response_for_create_workspace_invite(id = workspace_id)       

    def validate_input_data_for_create_workspace_invite(self,user_id:uuid,workspace_id:int,role:str):

        try:
            self.storage.valid_userid_field(id = user_id)
        except MissingId:
            self.presenter.raise_exception_for_missing_userid()

        try:
            self.storage.valid_id_field(id = workspace_id)
        except MissingId:
            self.presenter.raise_exception_for_missing_workspaceid()

        try:
            self.storage.valid_role_field(role = role)
        except MissingRole:
            self.presenter.raise_exception_for_missing_role()

    def accept_invitation(self,id:int):
        """
        ELP:
            check if input data exists
            check if invitation exists
            check if invitaion already accepted
            accept the invitation
        """
        try:
            self.storage.valid_id_field(id = id)
        except MissingId:
            self.presenter.raise_exception_for_missing_invite_id()

        try:
            self.storage.check_invitation(id = id)
        except InvalidInvitation:
            self.presenter.raise_exception_for_invalid_invite()

        try:
            self.storage.check_if_invitation_already_accepted(id = id)
        except AlreadyAccepted:
            self.presenter.raise_exception_for_invitation_already_accepted()

        self.storage.accept_invitation(id = id)

        return self.presenter.get_response_for_accept_invitation()

    def reject_invitation(self,id:int):
        """
        ELP:
            check if input data exists
            check if invitation exists
            check if invitaion already accepted
            accept the invitation
        """
        try:
            self.storage.valid_id_field(id = id)
        except MissingId:
            self.presenter.raise_exception_for_missing_invite_id()

        try:
            self.storage.check_invitation(id = id)
        except InvalidInvitation:
            self.presenter.raise_exception_for_invalid_invite()


        self.storage.reject_invitation(id = id)

        return self.presenter.get_response_for_reject_invitation()