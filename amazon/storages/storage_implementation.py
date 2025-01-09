from amazon.interactors.storage_interfaces.storage_interface import StorageInterface


class StorageImplementation(StorageInterface):

    def check_if_user_already_exists(self, email:str, contact_number:str):
        pass