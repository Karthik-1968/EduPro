import pytest
from django_swagger_utils.drf_server.exceptions import NotFound,Forbidden
from mock import create_autospec

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.workspace_invite_interactor import WorkspaceInviteInteractor
from type_form.exceptions.custom_exceptions import InvalidInvitationException,InvitationExpiredException

class TestRejectInvitationInteractor:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = WorkspaceInviteInteractor(storage = self.storage, presenter = self.presenter)
    
    def test_given_invalid_invite_id_raises_exception(self):
        
        invite_id = 1
        
        self.storage.check_invitation.side_effect = InvalidInvitationException
        self.presenter.raise_exception_for_invalid_invite.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.reject_invitation(invite_id = invite_id)
            
        self.storage.check_invitation.assert_called_once_with(id = invite_id)
        self.presenter.raise_exception_for_invalid_invite.assert_called_once()
        
    def test_invite_expired_raises_exception(self):
        
        invite_id = 1
        
        self.storage.check_if_invitation_expired.side_effect = InvitationExpiredException
        self.presenter.raise_exception_for_invitation_expired.side_effect = Forbidden
        
        with pytest.raises(Forbidden):
            self.interactor.reject_invitation(invite_id = invite_id)
            
        self.storage.check_if_invitation_expired.assert_called_once_with(id = invite_id)
        self.presenter.raise_exception_for_invitation_expired.assert_called_once()
        
    def test_reject_invitation(self):
        
        invite_id = 1
        
        expected_output= {"success":"invite rejected successfully"}
        
        self.storage.reject_invitation.return_value = None
        self.presenter.get_response_for_reject_invitation.return_value = expected_output
        
        actual_output = self.interactor.reject_invitation(invite_id = invite_id)
        
        assert actual_output == expected_output
        
        self.storage.reject_invitation.assert_called_once_with(id = invite_id)
        self.presenter.get_response_for_reject_invitation.assert_called_once_with()