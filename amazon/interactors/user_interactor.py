from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.exceptions.custom_exceptions import UserAlreadyExistsException, UserDoesNotExistException
from amazon.interactors.order_interactor import OrderInteractor
from amazon.interactors.storage_interfaces.dtos import UserDTO

class UserInteractor:
    
    def __init__(self, storage: UserStorageInterface, presenter: UserPresenterInterface):
        
        self.storage = storage
        self.presenter = presenter

    def create_user(self, user_dto:UserDTO):

        """ELP
            check if user already exists
            create_user
        """
        try:
            self.storage.check_if_user_already_exists(email=user_dto.email, contact_number=user_dto.contact_number)
        except UserAlreadyExistsException:
            self.presenter.raise_exception_for_user_already_exists()

        user_id = self.storage.create_user(user_dto=user_dto)

        return self.presenter.get_response_for_create_user(user_id=user_id)
    

    def get_user_details(self, user_id:str):

        """ELP
            -check if user_exists
            -get user details
        """
        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        order_details = OrderInteractor.get_orders_of_user(user_id=user_id)

        user_details=self.storage.get_user_details(user_id=user_id)

        return self.presenter.get_response_for_get_user_details(user_details=user_details,order_details=order_details)


