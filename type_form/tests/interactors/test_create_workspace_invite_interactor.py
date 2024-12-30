import pytest
from django_swagger_utils.drf_server.exceptions import NotFound,BadRequest
from mock import create_autospec

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.workspace_invite_interactor import WorkspaceInviteInteractor
from type_form.exceptions.custom_exceptions import InvalidUserException, InvalidWorkspaceException,\
    MaximumInvitesLimitReachedException, AlreadyInvitedException

class TestCreateWorkspaceInviteInteractor:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = WorkspaceInviteInteractor(storage = self.storage, presenter = self.presenter)
        
    def test_given_invalid_userid_raises_exception(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        workspace_id = 1
        role = "ADMIN"
        name = "My workspace invite"
        expiry_time = "2020-08-08 12:00:00"
        
        self.storage.check_user.side_effect = InvalidUserException
        self.presenter.raise_exception_for_invalid_user.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.create_workspace_invite(name=name, user_id=user_id, workspace_id=workspace_id, expiry_time=expiry_time,\
                role=role)
            
        self.storage.check_user.assert_called_once_with(id=user_id)
        self.presenter.raise_exception_for_invalid_user.assert_called_once()
        
    def test_given_invalid_workspace_id_raises_exception(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        workspace_id = 1
        role = "ADMIN"
        name = "My workspace invite"
        expiry_time = "2020-08-08 12:00:00"
        
        self.storage.check_workspace.side_effect = InvalidWorkspaceException
        self.presenter.raise_exception_for_invalid_workspace.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.create_workspace_invite(name=name, user_id=user_id, workspace_id=workspace_id, role=role, \
                expiry_time=expiry_time)
            
        self.storage.check_workspace.assert_called_once_with(id=workspace_id)
        self.presenter.raise_exception_for_invalid_workspace.assert_called_once()
        
    def test_if_invites_limit_reached_raises_exception(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        workspace_id = 1
        role = "ADMIN"
        name = "My workspace invite"
        expiry_time = "2020-08-08 12:00:00"
        
        self.storage.check_if_invites_limit_reached.side_effect = MaximumInvitesLimitReachedException
        self.presenter.raise_exception_for_maximum_invites_reached.side_effect = BadRequest
        
        with pytest.raises(BadRequest):
            self.interactor.create_workspace_invite(name=name,user_id=user_id, workspace_id=workspace_id, role=role, \
                expiry_time=expiry_time)
            
        self.storage.check_if_invites_limit_reached.assert_called_once_with(id=workspace_id)
        self.presenter.raise_exception_for_maximum_invites_reached.assert_called_once()
        
    def test_if_user_already_invited_raises_exception(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        workspace_id = 1
        role = "ADMIN"
        name = "My workspace invite"
        expiry_time = "2020-08-08 12:00:00"
        
        self.storage.check_if_user_already_invited.side_effect = AlreadyInvitedException
        self.presenter.raise_exception_for_user_already_invited.side_effect = BadRequest
        
        with pytest.raises(BadRequest):
            self.interactor.create_workspace_invite(name=name,user_id=user_id, workspace_id=workspace_id, role=role, \
                expiry_time=expiry_time)
            
        self.storage.check_if_user_already_invited.assert_called_once_with(user_id=user_id, workspace_id=workspace_id)
        self.presenter.raise_exception_for_user_already_invited.assert_called_once()
        
    def test_create_workspace_invite(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        workspace_id = 1
        role = "ADMIN"
        is_accepted = False
        name = "My workspace invite"
        expiry_time = "2020-08-08 12:00:00"
        
        expected_workspaceinvite_id = 1
        expected_workspaceinvite_id_dict = {"id": expected_workspaceinvite_id}
        
        self.storage.create_workspace_invite.return_value = expected_workspaceinvite_id
        self.presenter.get_response_for_create_workspace_invite.return_value = expected_workspaceinvite_id_dict
        
        actual_workspaceinvite_id_dict = self.interactor.create_workspace_invite(name=name,user_id=user_id, workspace_id=workspace_id,\
            role=role, expiry_time=expiry_time)
        
        assert actual_workspaceinvite_id_dict == expected_workspaceinvite_id_dict
        
        self.storage.create_workspace_invite.assert_called_once_with(name=name,user_id=user_id, workspace_id=workspace_id, role=role,\
            is_accepted=is_accepted, expiry_time=expiry_time)
        self.presenter.get_response_for_create_workspace_invite.assert_called_once_with(id=expected_workspaceinvite_id)
    