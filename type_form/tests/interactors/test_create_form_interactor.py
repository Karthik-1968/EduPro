from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import InvalidUserException, InvalidWorkspaceException, FormAlreadyExistsException
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from factory import Factory, Faker
from unittest.mock import create_autospec
from type_form.interactors.form_interactor import FormInteractor
from type_form.interactors.storage_interfaces.storage_interface import Formdto

    
class FormFactory(Factory):
    class Meta:
        model = Formdto

    user_id = Faker('uuid4')
    workspace_id = Faker('random_int', min=1, max=20)
    name = Faker('name')


class TestCreateFormInteractor:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = FormInteractor(storage=self.storage, presenter=self.presenter)
    
    def test_if_given_invalid_user_id_raises_exception(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        workspace_id = 1
        name = "My form"
        
        self.storage.check_user.side_effect = InvalidUserException
        self.presenter.raise_exception_for_invalid_user.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.create_form(user_id = user_id, workspace_id = workspace_id, name = name)
            
        self.storage.check_user.assert_called_once_with(id = user_id)
        self.presenter.raise_exception_for_invalid_user.assert_called_once()
        
    def test_if_given_invalid_workspace_id_raises_exception(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        workspace_id = 1
        name = "My form"
        
        self.storage.check_workspace.side_effect = InvalidWorkspaceException
        self.presenter.raise_exception_for_invalid_workspace.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.create_form(user_id = user_id, workspace_id = workspace_id, name = name)
            
        self.storage.check_user.assert_called_once_with(id = user_id)
        self.storage.check_workspace.assert_called_once_with(id = workspace_id)
        self.presenter.raise_exception_for_invalid_workspace.assert_called_once()
        
    def test_if_given_form_name_already_exists_raises_exception(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        workspace_id = 1
        name = "My form"
        
        self.storage.check_if_form_already_exists.side_effect = FormAlreadyExistsException
        self.presenter.raise_exception_for_form_already_exists.side_effect = BadRequest
        
        with pytest.raises(BadRequest):
            self.interactor.create_form(user_id = user_id, workspace_id = workspace_id, name = name)
            
        self.storage.check_user.assert_called_once_with(id = user_id)
        self.storage.check_workspace.assert_called_once_with(id = workspace_id)
        self.storage.check_if_form_already_exists.assert_called_once_with(name = name)
        self.presenter.raise_exception_for_form_already_exists.assert_called_once()
        
    def test_create_form_success(self):

        form = FormFactory()
        
        expected_form_id = 1
        expected_form_id_dict = {
            "form_id": expected_form_id
        }
        
        self.storage.create_form.return_value = expected_form_id
        self.presenter.get_response_for_create_form.return_value = expected_form_id_dict
        
        actual_form_id_dict = self.interactor.create_form(user_id = form.user_id, workspace_id = form.workspace_id, name = form.name)
        
        assert actual_form_id_dict == expected_form_id_dict
        
        self.storage.check_if_form_already_exists.assert_called_once_with(name = form.name)
        self.storage.create_form.assert_called_once_with(user_id = form.user_id, workspace_id = form.workspace_id, name = form.name)
        self.presenter.get_response_for_create_form.assert_called_once_with(id = expected_form_id)