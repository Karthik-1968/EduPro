import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.form_insights_interactor import FormInsightsInteractor
from type_form.exceptions.custom_exceptions import InvalidFormException

class TestCountSubmissionsOfFormInteractor:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = FormInsightsInteractor(storage=self.storage, presenter=self.presenter)
        
    def test_given_invalid_form_id_raises_exception(self):
        
        form_id = 1
        
        self.storage.check_form.side_effect = InvalidFormException
        self.presenter.raise_exception_for_invalid_form.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.count_submissions_of_form(form_id=form_id)
        
        self.storage.check_form.assert_called_once_with(id=form_id)
        self.presenter.raise_exception_for_invalid_form.assert_called_once()
        
    def test_given_valid_form_id_returns_submissions_count(self):
        
        form_id = 1
        count_of_submissions = 1
        expected_output = {"count_of_submissions": count_of_submissions}
        
        self.storage.get_submissions_count_of_form.return_value = count_of_submissions
        self.presenter.get_response_for_submissions_count_of_form.return_value = expected_output
    
        actual_output = self.interactor.count_submissions_of_form(form_id=form_id)
        
        assert actual_output == expected_output
    
        self.storage.check_form.assert_called_once_with(id=form_id)
        self.storage.get_submissions_count_of_form.assert_called_once_with(id=form_id)
        self.presenter.get_response_for_submissions_count_of_form.assert_called_once_with(count_of_submissions=count_of_submissions)