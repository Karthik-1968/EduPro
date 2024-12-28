from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.storage_interfaces.storage_interface import WorkspaceInvitedto
import uuid
from type_form.exceptions.custom_exceptions import InvalidUserException, InvalidWorkspaceException, AlreadyAcceptedException, \
    InvalidInvitationException, AlreadyInvitedException,MaximumInvitesLimitReachedException

class WorkspaceInviteInteractor:

    def __init__(self, storage:StorageInterface, presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    def create_workspace_invite(self, name:str, user_id:uuid, workspace_id:int, role:str, is_accepted:bool = False):

        """
            ELP:
                -validate input data
                    -validate user_id
                    -validate workspace_id
                    -validate role
                -check if user exists
                -check if workspace exists
                -check if exceeded maximum invites limit for workspace
                -check if already invited
                -create workspace invite
        """
        
        self.validate_input_data_for_create_workspace_invite(name =name, user_id = user_id, workspace_id = workspace_id, \
            role = role)

        try:
            self.storage.check_user(id = user_id)
        except InvalidUserException:
            self.presenter.raise_exception_for_invalid_user()

        try:
            self.storage.check_workspace(id = workspace_id)
        except InvalidWorkspaceException:
            self.presenter.raise_exception_for_invalid_workspace()
            
        try:
            self.storage.check_if_invites_limit_reached(id = workspace_id)
        except MaximumInvitesLimitReachedException:
            self.presenter.raise_exception_for_maximum_invites_reached()

        try:
            self.storage.check_if_user_already_invited(user_id = user_id, workspace_id = workspace_id)
        except AlreadyInvitedException:
            self.presenter.raise_exception_for_user_already_invited()

        workspace_id = self.storage.create_workspace_invite(name = name, user_id = user_id, workspace_id = workspace_id, role = role, is_accepted = is_accepted)

        return self.presenter.get_response_for_create_workspace_invite(id = workspace_id)       

    def validate_input_data_for_create_workspace_invite(self, name:str, user_id:uuid, workspace_id:int, role:str):
        
        name_not_present = not name
        if name_not_present:
            self.presenter.raise_exception_for_missing_invite_name()
        
        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_userid()

        workspace_id_not_present = not workspace_id
        if workspace_id_not_present:
            self.presenter.raise_exception_for_missing_workspaceid()
            
        role_not_present = not role
        if role_not_present:
            self.presenter.raise_exception_for_missing_role()


    def accept_invitation(self, invite_id:int):
        """
        ELP:
            -validate input data
                -validate invite_id
            -check if invitation exists
            -check if invitaion already accepted
            -accept the invitation
        """
        invite_id_not_present = not invite_id
        if invite_id_not_present:
            self.presenter.raise_exception_for_missing_invite_id()

        try:
            self.storage.check_invitation(id = invite_id)
        except InvalidInvitationException:
            self.presenter.raise_exception_for_invalid_invite()

        try:
            self.storage.check_if_invitation_already_accepted(id = invite_id)
        except AlreadyAcceptedException:
            self.presenter.raise_exception_for_invitation_already_accepted()

        self.storage.accept_invitation(id = invite_id)

        return self.presenter.get_response_for_accept_invitation()

    def reject_invitation(self, invite_id:int):
        """
        ELP:
            validate input data
                validate invite_id
            check if invitation exists
            reject the invitation
        """
        invite_id_not_present = not invite_id
        if invite_id_not_present:
            self.presenter.raise_exception_for_missing_invite_id()

        try:
            self.storage.check_invitation(id = invite_id)
        except InvalidInvitationException:
            self.presenter.raise_exception_for_invalid_invite()


        self.storage.reject_invitation(id = invite_id)

        return self.presenter.get_response_for_reject_invitation()
    
    
    def get_invites_of_workspace(self, workspace_id:int):

        """
            ELP:
               -validate input data
                -validate workspace_id
               -check if workspace exists
               -get list of invites of workspace
        """
        workspace_id_not_present = not workspace_id
        if workspace_id_not_present:
            self.presenter.raise_exception_for_missing_workspaceid()

        try:
            self.storage.check_workspace(id = workspace_id)
        except InvalidWorkspaceException:
            self.presenter.raise_exception_for_invalid_workspace()

        workspaceinvitedtos = self.storage.get_invites_of_workspace(id = workspace_id)

        return self.presenter.get_response_for_workspace_invites(workspaceinvitedtos = workspaceinvitedtos)