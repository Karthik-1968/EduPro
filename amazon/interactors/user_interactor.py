from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import UserAlreadyExistsException, UserDoesNotExistException
from amazon.interactors.order_interactor import OrderInteractor
from amazon.interactors.storage_interfaces.dtos import UserDTO

class UserInteractor:
    
    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def create_user(self, id:str, name:str, email:str, contact_number:str):

        """ELP
            validate_input_details
                -validate id
                -validate name
                -validate email
                -validate contact_number
            check if user already exists
            create_user
        """
        user_dto = UserDTO(id=id, name=name, email=email, contact_number=contact_number)

        self._validate_input_details_for_create_user(user_dto=user_dto)

        try:
            self.storage.check_if_user_already_exists(email=email, contact_number=contact_number)
        except UserAlreadyExistsException:
            self.presenter.raise_exception_for_user_already_exists()

        user_id = self.storage.create_user(user_dto=user_dto)

        return self.presenter.get_response_for_create_user(user_id=user_id)

    def _validate_input_details_for_create_user(self, user_dto:UserDTO):
        
        id_not_present = not user_dto.id
        if id_not_present:
            self.presenter.raise_exception_for_missing_user_id()
        
        name_not_present = not user_dto.name
        if name_not_present:
            self.presenter.raise_exception_for_missing_user_name()
        
        email_not_present = not user_dto.email
        if email_not_present:
            self.presenter.raise_exception_for_missing_email()
        
        contact_number_not_present = not user_dto.contact_number
        if contact_number_not_present:
            self.presenter.raise_exception_for_missing_contact_number()
    

    def get_user_details(self, user_id:str):

        """ELP
            -validate input data
                -validate user_id
            -check if user_exists
            -get user details
        """

        user_id_not_exists = not user_id
        if user_id_not_exists:
            self.presenter.raise_exception_for_missing_user_id()

        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        order_details = OrderInteractor.get_orders_of_user(user_id=user_id)

        user_details=self.storage.get_user_details(user_id=user_id)

        return self.presenter.get_response_for_get_user_details(user_details=user_details,order_details=order_details)


