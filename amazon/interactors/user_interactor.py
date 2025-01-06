from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import UserAlreadyExists, AddressAlreadyExists, UserDoesNotExist, AddressDoesNotExist,\
 AddressAlreadyAddedToUser, UserAddressDoesNotExist

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
        self.validate_input_details_for_create_user(id=id, name=name, email=email, contact_number=contact_number)
        try:
            self.storage.check_if_user_already_exists(email=email, contact_number=contact_number)
        except UserAlreadyExists:
            self.presenter.raise_exception_for_user_already_exists()

        user_id = self.storage.create_user(id=id, name=name, email=email, contact_number=contact_number)

        return self.presenter.get_response_for_create_user(user_id=user_id)

    def validate_input_details_for_create_user(self, id:str, name:str, email:str, contact_number:str):
        
        id_not_present = not id
        if id_not_present:
            self.presenter.raise_exception_for_missing_user_id()
        
        name_not_present = not name
        if name_not_present:
            self.presenter.raise_exception_for_missing_user_name()
        
        email_not_present = not email
        if email_not_present:
            self.presenter.raise_exception_for_missing_email()
        
        contact_number_not_present = not contact_number
        if contact_number_not_present:
            self.presenter.raise_exception_for_missing_contact_number()


    def create_address(self, door_no:str, street:str, city:str, district:str, state:str, country:str, pincode:str, contact_number:str, \
    address_type:str):

        """ELP
            validate_input_details
                -validate door no
                -validate street
                -validate city
                -validate district
                -validate state
                -validate country
                -validate pincode
                -validate contact_number
                -validate address_type
            check if address already exists
            create_address
        """
        self.validate_input_details_for_create_address(door_no=door_no, street=street, city=city, district=district, \
        state=state, country=country, pincode=pincode, contact_number=contact_number, address_type=address_type)

        try:
            self.storage.check_if_address_already_exists(door_no=door_no, street=street, city=city, district=district, \
            state=state, country=country, pincode=pincode)
        except AddressAlreadyExists:
            self.presenter.raise_exception_for_address_already_exists()

        address_id = self.storage.create_address(door_no=door_no, street=street, city=city, district=district, state=state, \
        country=country, pincode=pincode, contact_number=contact_number, address_type=address_type)

        return self.presenter.get_response_for_create_address(address_id=address_id)

    def validate_input_details_for_create_address(self, door_no:str, street:str, city:str, district:str, state:str, country:str, pincode:str, contact_number:str,\
     address_type:str):
        
        door_no_not_present = not door_no
        if door_no_not_present:
            self.presenter.raise_exception_for_missing_door_no()
        
        street_not_present = not street
        if street_not_present:
            self.presenter.raise_exception_for_missing_street()
        
        city_not_present = not city
        if city_not_present:
            self.presenter.raise_exception_for_missing_city()
        
        district_not_present = not district
        if district_not_present:
            self.presenter.raise_exception_for_missing_district()
        
        state_not_present = not state
        if state_not_present:
            self.presenter.raise_exception_for_missing_state()
        
        country_not_present = not country
        if country_not_present:
            self.presenter.raise_exception_for_missing_country()
        
        pincode_not_present = not pincode
        if pincode_not_present:
            self.presenter.raise_exception_for_missing_pincode()
        
        contact_number_not_present = not contact_number
        if contact_number_not_present:
            self.presenter.raise_exception_for_missing_contact_number()
        
        address_type_not_present = not address_type
        if address_type_not_present:
            self.presenter.raise_exception_for_missing_address_type()


    def add_address_to_user(self, user_id:str, address_id:str):

        """ELP
            validate_input_details
                -validate user_id
                -validate address_id
            check if user exists
            check if address exists
            check if address already added to user
            add_address_to_user
        """

        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_user_id()

        address_id_not_present = not address_id
        if address_id_not_present:
            self.presenter.raise_exception_for_missing_address_id()

        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except UserDoesNotExist:
            self.presenter.raise_exception_for_user_does_not_exist()

        try:
            self.storage.check_if_address_exists(address_id=address_id)
        except AddressDoesNotExist:
            self.presenter.raise_exception_for_address_does_not_exist()

        try:
            self.storage.check_if_address_already_added_to_user(user_id=user_id, address_id=address_id)
        except AddressAlreadyAddedToUser:
            self.presenter.raise_exception_for_address_already_added_to_user()

        useraddress_id = self.storage.add_address_to_user(user_id=user_id, address_id=address_id)

        return self.presenter.get_response_for_add_address_to_user(useraddress_id=useraddress_id)

    
    def update_user_address(self, useraddress_id:int, address_id:int):
        
        """ELP
            validate_input_details
                -validate useraddress_id
                -validate address_id
            check if useraddress exists
            check if address exists
            update_user_address
        """
        self.validate_input_details_for_update_user_address(useraddress_id=useraddress_id, address_id=address_id)

        try:
            self.storage.check_if_useraddress_exists(useraddress_id=useraddress_id)
        except UserAddressDoesNotExist:
            self.presenter.raise_exception_for_useraddress_does_not_exist()

        try:
            self.storage.check_if_address_exists(address_id=address_id)
        except AddressDoesNotExist:
            self.presenter.raise_exception_for_address_does_not_exist()

        self.storage.update_user_address(useraddress_id=useraddress_id, address_id=address_id)

        return self.presenter.get_response_for_update_user_address()

    def validate_input_details_for_update_user_address(self, useraddress_id:int, address_id:int):
        
        useraddress_id_not_present = not useraddress_id
        if useraddress_id_not_present:
            self.presenter.raise_exception_for_missing_useraddress_id()
        
        address_id_not_present = not address_id
        if address_id_not_present:
            self.presenter.raise_exception_for_missing_address_id()

    
    def update_user_name(self, user_id:int, name:str):
        
        """ELP
            validate_input_details
                -validate user_id
                -validate name
            check if user exists
            update_user_name
        """
        self.validate_input_details_for_update_user_name(user_id=user_id, name=name)

        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except UserDoesNotExist:
            self.presenter.raise_exception_for_user_does_not_exist()

        self.storage.update_user_name(user_id=user_id, name=name)

        return self.presenter.get_response_for_update_user_name()

    def validate_input_details_for_update_user_name(self, user_id:int, name:str):

        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_user_id()
        
        name_not_present = not name
        if name_not_present:
            self.presenter.raise_exception_for_missing_user_name()


    def update_user_email(self, user_id:int, email:str):
        
        """ELP
            validate_input_details
                -validate user_id
                -validate email
            check if user exists
            update_user_email
        """
        self.validate_input_details_for_update_user_email(user_id=user_id, email=email)

        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except UserDoesNotExist:
            self.presenter.raise_exception_for_user_does_not_exist()

        self.storage.update_user_email(user_id=user_id, email=email)

        return self.presenter.get_response_for_update_user_email()

    def validate_input_details_for_update_user_email(self, user_id:int, email:str):

        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_user_id()
        
        email_not_present = not email
        if email_not_present:
            self.presenter.raise_exception_for_missing_email()


    def update_user_contact_number(self, user_id:int, contact_number:str):
        
        """ELP
            validate_input_details
                -validate user_id
                -validate contact_number
            check if user exists
            update_contact_number
        """
        self.validate_input_details_for_update_contact_number(user_id=user_id, contact_number=contact_number)

        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except UserDoesNotExist:
            self.presenter.raise_exception_for_user_does_not_exist()

        self.storage.update_user_contact_number(user_id=user_id, contact_number=contact_number)

        return self.presenter.get_response_for_update_user_contact_number()

    def validate_input_details_for_update_contact_number(self, user_id:int, contact_number:str):

        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_user_id()
        
        contact_number_not_present = not contact_number
        if contact_number_not_present:
            self.presenter.raise_exception_for_missing_contact_number()

    
    def delete_user_address(self,useraddress_id:int):

        useraddress_id_not_present = not useraddress_id
        if useraddress_id_not_present:
            self.presenter.raise_exception_for_missing_useraddress_id()

        try:
            self.storage.check_if_useraddress_exists(useraddress_id=useraddress_id)
        except UserAddressDoesNotExist:
            self.presenter.raise_exception_for_useraddress_does_not_exist()

        self.storage.delete_user_address(useraddress_id=useraddress_id)

        return self.presenter.get_response_for_delete_user_address()
