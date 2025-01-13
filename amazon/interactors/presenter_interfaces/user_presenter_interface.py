from abc import abstractmethod

class UserPresenterInterface:

    @abstractmethod
    def raise_exception_for_user_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_user(self, user_id:str):
        pass

    @abstractmethod
    def raise_exception_for_address_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_address(self, address_id:str):
        pass

    @abstractmethod
    def raise_exception_for_user_does_not_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_address_does_not_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_address_already_added_to_user(self):
        pass

    @abstractmethod
    def get_response_for_add_address_to_user(self, useraddress_id:str):
        pass

    @abstractmethod
    def raise_exception_for_useraddress_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_update_user_address(self):
        pass

    @abstractmethod
    def get_response_for_update_user_name(self):
        pass

    @abstractmethod
    def get_response_for_update_user_email(self):
        pass

    @abstractmethod
    def get_response_for_update_user_contact_number(self):
        pass

    @abstractmethod
    def get_response_for_delete_user_address(self):
        pass

    @abstractmethod
    def get_response_for_get_user_details(self,user_details:dict,order_details:list[dict])->dict:
        pass