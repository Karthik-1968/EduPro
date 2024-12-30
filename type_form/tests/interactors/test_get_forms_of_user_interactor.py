from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import InvalidUserException, InvalidWorkspaceException
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from type_form.interactors.form_interactor import FormInteractor
from type_form.interactors.storage_interfaces.storage_interface import FormDTO

    
class TestGetFormsOfUser:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = FormInteractor(storage=self.storage, presenter=self.presenter)
    
    def test_if_given_invalid_user_id_raises_exception(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        
        self.storage.check_user.side_effect = InvalidUserException
        self.presenter.raise_exception_for_invalid_user.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.get_forms_of_user(user_id = user_id)
            
        self.storage.check_user.assert_called_once_with(id = user_id)
        self.presenter.raise_exception_for_invalid_user.assert_called_once()
        
    def test_get_all_forms_for_the_valid_user(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        
        expected_formdtos = [
            FormDTO(
                user_id = user_id,
                workspace_id = 1,
                name = "My form"
            ),
            FormDTO(
                user_id = user_id,
                workspace_id = 2,
                name = "My form2"
            )
        ]
        
        expected_formdetails_dict = [
            {
                "user_id":formdto.user_id,
                "workspace_id":formdto.workspace_id,
                "name":formdto.name
            }
            for formdto in expected_formdtos
        ]
        
        self.storage.get_forms_of_user.return_value = expected_formdtos
        self.presenter.get_response_for_forms_of_user.return_value = expected_formdetails_dict
        
        actual_formdetials_dict = self.interactor.get_forms_of_user(user_id = user_id)
        
        assert actual_formdetials_dict == expected_formdetails_dict
        
        self.storage.check_user.assert_called_once_with(id = user_id)
        self.storage.get_forms_of_user.assert_called_once_with(id = user_id)
        self.presenter.get_response_for_forms_of_user.assert_called_once_with(formdtos = expected_formdtos)