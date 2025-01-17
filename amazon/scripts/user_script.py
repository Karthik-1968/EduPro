from amazon.models import User
from amazon.models import Address
from amazon.models import UserAddress

def create_user():

    user_data = [
    {"id": "44ba532c-40a1-46da-8528-2e395576c131", "name": "Karthik", "email": "dayanakarthik28@gmail.com", "contact_number": "9876543210"},
    {"id": "550e8400-e29b-41d4-a716-446655440001", "name": "Sandeep", "email": "sandeepchowdary39@gmail.com", "contact_number": "9123456789"},
    {"id": "550e8400-e29b-41d4-a716-446655440002", "name": "Chaitanya", "email": "chaitanyapatcherla46@gmail.com", "contact_number": "9234567890"},
    {"id": "550e8400-e29b-41d4-a716-446655440003", "name": "Joshi", "email": "joshiparam34@gmail.com", "contact_number": "9345678901"},
    {"id": "550e8400-e29b-41d4-a716-446655440004", "name": "Aditya", "email": "adityapilli31@gmail.com", "contact_number": "9456789012"}
    ]

    for data in user_data:

        User.objects.create(id=data['id'], name=data['name'], email=data['email'], contact_number=data['contact_number'])

def create_address():

    address_data = [
    {"id": 1, "door_no": "123", "street": "Main Street", "city": "New York", "district": "Manhattan", "state": "NY", "country": "USA", "pincode": "10001", "contact_number": "9876543210", "address_type": "house"},
    {"id": 2, "door_no": "456", "street": "Second Avenue", "city": "Los Angeles", "district": "Downtown", "state": "CA", "country": "USA", "pincode": "90001", "contact_number": "9123456789", "address_type": "apartment"},
    {"id": 3, "door_no": "789", "street": "Park Street", "city": "San Francisco", "district": "Central", "state": "CA", "country": "USA", "pincode": "94101", "contact_number": "9234567890", "address_type": "business"},
    {"id": 4, "door_no": "101", "street": "Lake Drive", "city": "Chicago", "district": "North", "state": "IL", "country": "USA", "pincode": "60601", "contact_number": "9345678901", "address_type": "other"},
    {"id": 5, "door_no": "202", "street": "Broadway", "city": "Seattle", "district": "Downtown", "state": "WA", "country": "USA", "pincode": "98101", "contact_number": "9456789012", "address_type": "house"}
]
    for data in address_data:

        Address.objects.create(id=data['id'], door_no=data['door_no'], street=data['street'], city=data['city'], \
                               district=data['district'], state=data['state'], country=data['country'], pincode=data['pincode'], \
                                contact_number=data['contact_number'], address_type=data['address_type'])
        
def add_address_to_user():

    add_address_to_user_data = [
    {"id": 1, "user_id": "44ba532c-40a1-46da-8528-2e395576c131", "address_id": 1},
    {"id": 2, "user_id": "550e8400-e29b-41d4-a716-446655440001", "address_id": 2},
    {"id": 3, "user_id": "550e8400-e29b-41d4-a716-446655440002", "address_id": 3},
    {"id": 4, "user_id": "550e8400-e29b-41d4-a716-446655440003", "address_id": 4},
    {"id": 5, "user_id": "550e8400-e29b-41d4-a716-446655440004", "address_id": 5}
]
    for data in add_address_to_user_data:

        user_id = data['user_id']
        address_id = data['address_id']
        UserAddress.objects.create(id=data['id'], user_id=user_id, address_id=address_id)