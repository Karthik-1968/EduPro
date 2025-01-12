from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions import custom_exceptions
from amazon.interactors.storage_interfaces.storage_interface import AddressDTO


class AddressInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    
    def create_address(self, address_dto:AddressDTO):

        """ELP
            check if address already exists
            create_address
        """
        try:
            self.storage.check_if_address_already_exists(address_dto=address_dto)
        except custom_exceptions.AddressAlreadyExistsException:
            self.presenter.raise_exception_for_address_already_exists()

        address_id = self.storage.create_address(address_dto=address_dto)

        return self.presenter.get_response_for_create_address(address_id=address_id)


    def add_address_to_user(self, user_id:str, address_id:int):

        """ELP
            check if user exists
            check if address exists
            check if address already added to user
            add_address_to_user
        """
        self._check_if_input_data_is_correct_for_add_address_to_user(user_id=user_id, address_id=address_id)

        useraddress_id = self.storage.add_address_to_user(user_id=user_id, address_id=address_id)

        return self.presenter.get_response_for_add_address_to_user(useraddress_id=useraddress_id)
    
    def _check_if_input_data_is_correct_for_add_address_to_user(self, user_id:str, address_id:int):

        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except custom_exceptions.UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        try:
            self.storage.check_if_address_exists(address_id=address_id)
        except custom_exceptions.AddressDoesNotExistException:
            self.presenter.raise_exception_for_address_does_not_exist()

        try:
            self.storage.check_if_address_already_added_to_user(user_id=user_id, address_id=address_id)
        except custom_exceptions.AddressAlreadyAddedToUserException:
            self.presenter.raise_exception_for_address_already_added_to_user()

    
    def update_user_address(self, useraddress_id:int, address_id:int):
        
        """ELP
            check if useraddress exists
            check if address exists
            update_user_address
        """
        try:
            self.storage.check_if_useraddress_exists(useraddress_id=useraddress_id)
        except custom_exceptions.UserAddressDoesNotExistException:
            self.presenter.raise_exception_for_useraddress_does_not_exist()

        try:
            self.storage.check_if_address_exists(address_id=address_id)
        except custom_exceptions.AddressDoesNotExistException:
            self.presenter.raise_exception_for_address_does_not_exist()

        self.storage.update_user_address(useraddress_id=useraddress_id, address_id=address_id)

        return self.presenter.get_response_for_update_user_address()

    
    def update_user_name(self, user_id:str, name:str):
        
        """ELP
            check if user exists
            update_user_name
        """
        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except custom_exceptions.UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        self.storage.update_user_name(user_id=user_id, name=name)

        return self.presenter.get_response_for_update_user_name()


    def update_user_email(self, user_id:str, email:str):
        
        """ELP
            check if user exists
            update_user_email
        """
        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except custom_exceptions.UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        self.storage.update_user_email(user_id=user_id, email=email)

        return self.presenter.get_response_for_update_user_email()


    def update_user_contact_number(self, user_id:str, contact_number:str):
        
        """ELP
            check if user exists
            update_contact_number
        """
        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except custom_exceptions.UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        self.storage.update_user_contact_number(user_id=user_id, contact_number=contact_number)

        return self.presenter.get_response_for_update_user_contact_number()

    
    def delete_user_address(self, useraddress_id:int):

        try:
            self.storage.check_if_useraddress_exists(useraddress_id=useraddress_id)
        except custom_exceptions.UserAddressDoesNotExistException:
            self.presenter.raise_exception_for_useraddress_does_not_exist()

        self.storage.delete_user_address(useraddress_id=useraddress_id)

        return self.presenter.get_response_for_delete_user_address()