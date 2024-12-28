import pytest
from django_swagger_utils.drf_server.exceptions import NotFound,BadRequest
from mock import create_autospec
from factory import Factory, Faker, SubFactory

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.workspace_interactor import WorkspaceInteractor
from type_form.exceptions.custom_exceptions import InvalidUserException,WorkspaceAlreadyExistsException
from type_form.interactors.storage_interfaces.storage_interface import Userdto,Workspacedto


class UserFactory(Factory):
    class Meta:
        model = Userdto

    id = Faker('uuid4')
    email = Faker('email')


class WorkspaceFactory(Factory):
    class Meta:
        model = Workspacedto

    user = SubFactory(UserFactory)
    name = Faker('name')
    is_private = Faker('boolean')
    max_invites = Faker('random_int', min=1, max=20)
    

class TestCreateWorkspaceInteractor:
    
    def test_given_invalid_user_id_raises_exception(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        name = "My workspace"
        
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        
        interactor = WorkspaceInteractor(storage = storage, presenter = presenter)
        
        storage.check_user.side_effect = InvalidUserException
        presenter.raise_exception_for_invalid_user.side_effect = NotFound
        
        with pytest.raises(NotFound):
            interactor.create_workspace(user_id = user_id, name = name)
            
        storage.check_user.assert_called_once_with(id = user_id)
        presenter.raise_exception_for_invalid_user.assert_called_once()
        
    def test_given_workspace_already_exists_exception(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        name = "My workspace"
        
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        
        interactor = WorkspaceInteractor(storage = storage, presenter = presenter)
        
        storage.check_if_workspace_already_exists.side_effect = WorkspaceAlreadyExistsException
        presenter.raise_exception_for_workspace_already_exists.side_effect = BadRequest
        
        with pytest.raises(BadRequest):
            interactor.create_workspace(user_id = user_id, name = name)
            
        storage.check_if_workspace_already_exists.assert_called_once_with(name = name)
        presenter.raise_exception_for_workspace_already_exists.assert_called_once()

    def test_given_valid_userid_creates_workspace_and_returns_workspaceid_int(self):
        
        user = UserFactory
        workspace = WorkspaceFactory(user = user)
        
        expected_workspace_id = 1
        expected_workspace_id_dict = {
            "workspace_id": expected_workspace_id
        }
        
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        
        interactor = WorkspaceInteractor(storage = storage, presenter = presenter)
        
        storage.get_user.return_value = user
        storage.create_workspace.return_value = expected_workspace_id
        presenter.get_response_for_create_workspace.return_value = expected_workspace_id_dict
        
        actual_workspace_id_dict = interactor.create_workspace(user_id = user.id, name = workspace.name, is_private = workspace.is_private, max_invites = workspace.max_invites)
        
        assert expected_workspace_id_dict == actual_workspace_id_dict
        
        storage.check_user.assert_called_once_with(id = user.id)
        storage.check_if_workspace_already_exists.assert_called_once_with(name = workspace.name)
        storage.get_user.assert_called_once_with(id = user.id)
        storage.create_workspace.assert_called_once_with(workspacedto = workspace)
        presenter.get_response_for_create_workspace.assert_called_once_with(workspace_id = expected_workspace_id)
        
        
        