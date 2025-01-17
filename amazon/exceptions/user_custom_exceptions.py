class UserAlreadyExistsException(Exception):
    pass

class AddressAlreadyExistsException(Exception):
    pass

class UserDoesNotExistException(Exception):
    def __init__(self, user_id:str):
        self.user_id = user_id
    
    def __str__(self):
        return f"{self.user_id} does not exist"

class AddressDoesNotExistException(Exception):
    def __init__(self, address_id:int):
        self.address_id = address_id

    def __str__(self):
        return f"{self.address_id} does not exist"

class AddressAlreadyAddedToUserException(Exception):
    def __init__(self, address_id:int, user_id:str):
        self.address_id = address_id
        self.user_id = user_id

    def __str__(self):
        return f"{self.address_id} already added to {self.user_id}"

class UserAddressDoesNotExistException(Exception):
    def __init(self, useraddress_id:int):
        self.useraddress_id = useraddress_id
    
    def __str__(self):
        return f"{self.useraddress_id} does not exist"
