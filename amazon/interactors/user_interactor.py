from amazon.interactors.storage_interfaces import storage_interface
from amazon.interactors.presenter_interfaces import presenter_interface
from amazon.exceptions.custom_exception import UserAlreadyExists, AddressAlreadyExists, UserDoesNotExist, AddressDoesNotExist,\
 AddressAlreadyAddedToUser

class UserInteractor:
    
    def __init__(self, storage: storage_interface, presenter: presenter_interface):
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

    def create_address(self, street:str, city:str, district:str, state:str, country:str, pincode:str, contact_number:str, \
    address_type:str):

        """ELP
            validate_input_details
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
        self.validate_input_details_for_create_address(street=street, city=city, district=district, state=state, country=country, pincode=pincode,\
         contact_number=contact_number, address_type=address_type)

         try:
            self.storage.check_if_address_already_exists(street=street, city=city, district=district, state=state, country=country, pincode=pincode)
        except AddressAlreadyExists:
            self.presenter.raise_exception_for_address_already_exists()

        address_id = self.storage.create_address(street=street, city=city, district=district, state=state, country=country, \
        pincode=pincode, contact_number=contact_number, address_type=address_type)

        return self.presenter.get_response_for_create_address(address_id=address_id)

    def validate_input_details_for_create_address(self, street:str, city:str, district:str, state:str, country:str, pincode:str, contact_number:str,\
     address_type:str):
        
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