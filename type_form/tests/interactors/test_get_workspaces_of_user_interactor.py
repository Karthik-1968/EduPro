import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec
from factory import Factory, Faker, SubFactory

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.workspace_interactor import WorkspaceInteractor
from type_form.exceptions.custom_exceptions import InvalidUserException
from type_form.interactors.storage_interfaces.storage_interface import Userdto,Workspacedto
from type_form.interactors.storage_interfaces.storage_interface import Userdto, Workspacedto

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
        
class TestGetWorkspacesOfUser:
            
    def test_given_invalid_user_id_raises_exception(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        name = "My workspace"
        
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        
        interactor = WorkspaceInteractor(storage=storage, presenter=presenter)
        
        storage.check_user.side_effect = InvalidUserException
        presenter.raise_exception_for_invalid_user.side_effect = NotFound
        
        with pytest.raises(NotFound):
            interactor.create_workspace(user_id=user_id, name=name)
            
        storage.check_user.assert_called_once_with(id=user_id)
        presenter.raise_exception_for_invalid_user.assert_called_once()
        
    def test_given_userid_return_list_of_workspaces(self):
        
        user = UserFactory()
        
        expected_workspacedtos = [
            Workspacedto(
                user=user,
                name="FirstWorkspace",
                is_private=False,
                max_invites=10
            ),
            Workspacedto(
                user=user,
                name="SecondWorkspace",
                is_private=True,
                max_invites=5
            )
        ]
        
        expected_output = [
            {
                "name": "FirstWorkspace",
                "is_private": False,
                "max_invites": 10
            },
            {
                "name": "SecondWorkspace",
                "is_private": True,
                "max_invites": 5
            }
        ]
        
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        
        interactor = WorkspaceInteractor(storage=storage, presenter=presenter)
        
        storage.get_workspaces_of_user.return_value = expected_workspacedtos
        presenter.get_response_for_workspaces_of_user.return_value = expected_output
        
        actual_output = interactor.get_workspaces_of_user(user_id=user.id)
        
        assert expected_output == actual_output
        
        storage.check_user.assert_called_once_with(id=user.id)
        storage.get_workspaces_of_user.assert_called_once_with(id=user.id)
        presenter.get_response_for_workspaces_of_user.assert_called_once_with(workspacedtos=expected_workspacedtos)
        
    def test_given_userid_with_no_workspaces_returns_empty_list(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        
        expected_workspacedtos = []
        expected_output = []
        
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        
        interactor = WorkspaceInteractor(storage=storage, presenter=presenter)
        
        storage.get_workspaces_of_user.return_value = expected_workspacedtos
        presenter.get_response_for_workspaces_of_user.return_value = expected_output
        
        actual_output = interactor.get_workspaces_of_user(user_id=user_id)
        
        assert expected_output == actual_output
        
        storage.check_user.assert_called_once_with(id=user_id)
        storage.get_workspaces_of_user.assert_called_once_with(id=user_id)
        presenter.get_response_for_workspaces_of_user.assert_called_once_with(workspacedtos=expected_workspacedtos)