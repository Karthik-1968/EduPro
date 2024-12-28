import pytest
from django_swagger_utils.drf_server.exceptions import NotFound,BadRequest
from mock import create_autospec

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.workspace_invite_interactor import WorkspaceInviteInteractor
from type_form.exceptions.custom_exceptions import InvalidInvitationException,AlreadyAcceptedException
    
class TestAcceptInvitationInteractor:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = WorkspaceInviteInteractor(storage = self.storage, presenter = self.presenter)
    
    def test_given_invalid_invite_id_raises_exception(self):
        
        invite_id = 1
        
        self.storage.check_invitation.side_effect = InvalidInvitationException
        self.presenter.raise_exception_for_invalid_invite.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.accept_invitation(invite_id = invite_id)
            
        self.storage.check_invitation.assert_called_once_with(id = invite_id)
        self.presenter.raise_exception_for_invalid_invite.assert_called_once()
        
    def test_given_already_accepted_invite_raises_exception(self):
        
        invite_id = 1
        
        self.storage.check_if_invitation_already_accepted.side_effect = AlreadyAcceptedException
        self.presenter.raise_exception_for_invitation_already_accepted.side_effect = BadRequest
        
        with pytest.raises(BadRequest):
            self.interactor.accept_invitation(invite_id = invite_id)
            
        self.storage.check_if_invitation_already_accepted.assert_called_once_with(id = invite_id)
        self.presenter.raise_exception_for_invitation_already_accepted.assert_called_once()
        
    def test_accept_invitation(self):
        
        invite_id = 1
        
        expected_output= {"message":"Invite accepted successfully"}
        
        self.storage.accept_invitation.return_value = None
        self.presenter.get_response_for_accept_invitation.return_value = expected_output
        
        actual_output = self.interactor.accept_invitation(invite_id = invite_id)
        
        assert actual_output == expected_output
        
        self.storage.accept_invitation.assert_called_once_with(id = invite_id)
        self.presenter.get_response_for_accept_invitation.assert_called_once_with()