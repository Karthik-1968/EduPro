from abc import abstractmethod
from amazon.interactors.storage_interfaces.dtos import UserDTO, AddressDTO

class UserStorageInterface:

    @abstractmethod
    def check_if_user_already_exists(self, email:str, contact_number:str):
        pass

    @abstractmethod
    def create_user(self, user_dto:UserDTO)->str:
        pass

    @abstractmethod
    def check_if_address_already_exists(self, address_dto:AddressDTO):
        pass

    @abstractmethod
    def create_address(self, address_dto:AddressDTO)->int:
        pass

    @abstractmethod
    def check_if_user_exists(self, user_id:str):
        pass

    @abstractmethod
    def check_if_address_exists(self, address_id:int):
        pass

    @abstractmethod
    def check_if_address_already_added_to_user(self, user_id:str, address_id:int):
        pass

    @abstractmethod
    def add_address_to_user(self, user_id:str, address_id:int)->int:
        pass

    @abstractmethod
    def check_if_useraddress_exists(self, useraddress_id:int):
        pass

    @abstractmethod
    def update_user_address(self, useraddress_id:int, address_id:int):
        pass

    @abstractmethod
    def update_user_name(self, user_id:str, name:str):
        pass

    @abstractmethod
    def update_user_email(self, user_id:str, email:str):
        pass

    @abstractmethod
    def update_user_contact_number(self, user_id:str, contact_number:str):
        pass

    @abstractmethod
    def delete_user_address(self, useraddress_id:int):
        pass

    @abstractmethod
    def get_user_details(self,user_id:str)->dict:
        pass