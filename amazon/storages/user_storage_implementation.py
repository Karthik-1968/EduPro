from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.storage_interfaces.dtos import UserDTO, AddressDTO
from amazon.models import User, Address, UserAddress
from amazon.exceptions import user_custom_exceptions

class UserStorageImplementation(UserStorageInterface):

    def check_if_user_already_exists(self, email:str, contact_number:str):
        
        if User.objects.filter(email=email).exists():
            raise user_custom_exceptions.UserAlreadyExistsException()
        
        elif User.objects.filter(contact_number=contact_number).exists():
            raise user_custom_exceptions.UserAlreadyExistsException()
        
    def create_user(self, user_dto:UserDTO)->str:

        user = User.objects.create(
            id=user_dto.id,
            name=user_dto.name,
            email=user_dto.email,
            contact_number=user_dto.contact_number,
        )

        return user.id
    
    def check_if_address_already_exists(self, address_dto:AddressDTO):

        if Address.objects.filter(door_no=address_dto.door_no, street=address_dto.street, city=address_dto.city, \
                                  district=address_dto.district, state=address_dto.state, country=address_dto.country, \
                                    pincode=address_dto.pincode, contact_number=address_dto.contact_number, \
                                        address_type=address_dto.address_type).exists():
            raise user_custom_exceptions.AddressAlreadyExistsException()
        
    def create_address(self, address_dto:AddressDTO)->int:

        address = Address.objects.create(
            id=address_dto.id,
            door_no=address_dto.door_no,
            street=address_dto.street,
            city=address_dto.city,
            district=address_dto.district,
            state=address_dto.state,
            country=address_dto.country,
            pincode=address_dto.pincode,
            contact_number=address_dto.contact_number,
            address_type=address_dto.address_type
        )

        return address.id
    
    def check_if_user_exists(self, user_id:str):

        user = User.objects.filter(id=user_id).exists()
        user_not_exists = not user
        if user_not_exists:
            raise user_custom_exceptions.UserDoesNotExistException(user_id=user_id)
        
    def check_if_address_exists(self, address_id:int):

        address = Address.objects.filter(id=address_id).exists()
        address_not_exists = not address
        if address_not_exists:
            raise user_custom_exceptions.AddressDoesNotExistException(address_id=address_id)
        
    def check_if_address_already_added_to_user(self, user_id:str, address_id:int):

        if UserAddress.objects.filter(user_id=user_id, address_id=address_id).exists():
            raise user_custom_exceptions.AddressAlreadyAddedToUserException(address_id=address_id, user_id=user_id)
        
    def add_address_to_user(self, user_id:str, address_id:int):
        
        UserAddress.objects.create(
            user_id=user_id,
            address_id=address_id
        )
