from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import InvalidFormException

class FormInsightsInteractor:

    def __init__(self, storage:StorageInterface, presenter:PresenterInterface):
        
        self.storage = storage
        self.presenter = presenter

    def get_views_of_form(self, form_id:int):
        """
            ELP:
                -validate input data
                    -validate form_id
                -check if form exists
                -get views of form
        """

        form_id_not_present = not form_id
        if form_id_not_present:
            self.presenter.raise_exception_for_missing_formid()
        
        try:
            self.storage.check_form(id = form_id)
        except InvalidFormException:
            self.presenter.raise_exception_for_invalid_form()

        count_of_views = self.storage.get_views_of_form(id = form_id)

        return self.presenter.get_response_for_views_of_form(count_of_views = count_of_views)

    

    def get_submissions_of_form(self, form_id:int):
        """
            ELP:
                -validate input data
                    -validate form_id
                -check if form exists
                -get submissions of form
        """
        form_id_not_present = not form_id
        if form_id_not_present:
            self.presenter.raise_exception_for_missing_formid()
        
        try:
            self.storage.check_form(id = form_id)
        except InvalidFormException:
            self.presenter.raise_exception_for_invalid_form()

        count_of_submissions = self.storage.get_submissions_of_form(id = form_id)

        return self.presenter.get_response_for_submissions_of_form(count_of_submissions = count_of_submissions)

    
    
    def get_form_completionrate(self, form_id:int):

        """
            ELP:
                -validate input data
                    -validate form_id
                -check if form exists
                -get completionrate of form
        """
        form_id_not_present = not form_id
        if form_id_not_present:
            self.presenter.raise_exception_for_missing_formid()
        
        try:
            self.storage.check_form(id = form_id)
        except InvalidFormException:
            self.presenter.raise_exception_for_invalid_form()

        completion_rate = self.storage.get_form_completionrate(id = form_id)

        return self.presenter.get_response_for_from_completionrate(completion_rate = completion_rate)