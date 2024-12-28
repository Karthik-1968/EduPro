import pytest
from django_swagger_utils.drf_server.exceptions import NotFound,BadRequest
from mock import create_autospec

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.workspace_invite_interactor import WorkspaceInviteInteractor
from type_form.exceptions.custom_exceptions import InvalidWorkspaceException
from type_form.interactors.storage_interfaces.storage_interface import WorkspaceInvitedto

class TestGetInvitesOfWorkspaceInteractor:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = WorkspaceInviteInteractor(storage = self.storage, presenter = self.presenter)
        
    def test_given_invalid_workspace_id_raises_exception(self):
        
        workspace_id = 1
        
        self.storage.check_workspace.side_effect = InvalidWorkspaceException
        self.presenter.raise_exception_for_invalid_workspace.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.get_invites_of_workspace(workspace_id = workspace_id)
            
        self.storage.check_workspace.assert_called_once_with(id = workspace_id)
        self.presenter.raise_exception_for_invalid_workspace.assert_called
        
    def test_get_invites_of_workspace(self):
        
        workspace_id = 1
        
        workspace_invite_dtos = [
            WorkspaceInvitedto(name = "My invite 1", user_id = "550e8400-e29b-41d4-a716-446655440000", workspace_id = 1, role = "ADMIN"\
                , is_accepted = False),
            WorkspaceInvitedto(name = "My invite 2", user_id = "650e8445-e29b-41d4-a716-446655440000", workspace_id = 1, role = "CUSTOMER"\
                , is_accepted = False)
        ]
        
        expected_output= [
            {
                "name":"My invite 1",
                "role":"ADMIN",
                "is_accepted":False
            },
            {
                "name":"My invite 2",
                "role":"CUSTOMER",
                "is_accepted":False
            }
        ]
        
        self.storage.get_invites_of_workspace.return_value = workspace_invite_dtos
        self.presenter.get_response_for_workspace_invites.return_value = expected_output
        
        actual_output = self.interactor.get_invites_of_workspace(workspace_id = workspace_id)
        
        assert actual_output == expected_output
        
        self.storage.get_invites_of_workspace.assert_called_once_with(id = workspace_id)
        self.presenter.get_response_for_workspace_invites.assert_called_once_with(workspaceinvitedtos = workspace_invite_dtos)