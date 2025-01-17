from amazon.models import Item
from amazon.models import Property
from amazon.models import ItemProperty

def create_item():

    items_data = [
    # Electronics
    {"id": 1, "category_id": 1, "item_name": "Smartphone", "price": 699.99, "number_of_left_in_stock": 50, "number_of_purchases_in_last_month": 10, "views": 100},
    {"id": 2, "category_id": 1, "item_name": "Laptop", "price": 999.99, "number_of_left_in_stock": 30, "number_of_purchases_in_last_month": 8, "views": 120},
    {"id": 3, "category_id": 1, "item_name": "Smartwatch", "price": 199.99, "number_of_left_in_stock": 70, "number_of_purchases_in_last_month": 15, "views": 90},
    {"id": 4, "category_id": 1, "item_name": "Wireless Earbuds", "price": 129.99, "number_of_left_in_stock": 150, "number_of_purchases_in_last_month": 40, "views": 200},
    {"id": 5, "category_id": 1, "item_name": "Tablet", "price": 499.99, "number_of_left_in_stock": 60, "number_of_purchases_in_last_month": 12, "views": 110},

    # Books
    {"id": 6, "category_id": 2, "item_name": "Fiction Novel", "price": 19.99, "number_of_left_in_stock": 200, "number_of_purchases_in_last_month": 50, "views": 300},
    {"id": 7, "category_id": 2, "item_name": "Non-Fiction Book", "price": 25.99, "number_of_left_in_stock": 150, "number_of_purchases_in_last_month": 30, "views": 250},
    {"id": 8, "category_id": 2, "item_name": "Comic Book", "price": 12.99, "number_of_left_in_stock": 300, "number_of_purchases_in_last_month": 60, "views": 400},
    {"id": 9, "category_id": 2, "item_name": "Educational Textbook", "price": 49.99, "number_of_left_in_stock": 100, "number_of_purchases_in_last_month": 20, "views": 150},
    {"id": 10, "category_id": 2, "item_name": "Biography", "price": 29.99, "number_of_left_in_stock": 120, "number_of_purchases_in_last_month": 25, "views": 180},

    # Clothing
    {"id": 11, "category_id": 3, "item_name": "T-Shirt", "price": 15.99, "number_of_left_in_stock": 100, "number_of_purchases_in_last_month": 40, "views": 80},
    {"id": 12, "category_id": 3, "item_name": "Jeans", "price": 49.99, "number_of_left_in_stock": 80, "number_of_purchases_in_last_month": 25, "views": 100},
    {"id": 13, "category_id": 3, "item_name": "Jacket", "price": 99.99, "number_of_left_in_stock": 50, "number_of_purchases_in_last_month": 10, "views": 70},
    {"id": 14, "category_id": 3, "item_name": "Sweater", "price": 59.99, "number_of_left_in_stock": 60, "number_of_purchases_in_last_month": 15, "views": 65},
    {"id": 15, "category_id": 3, "item_name": "Shoes", "price": 89.99, "number_of_left_in_stock": 70, "number_of_purchases_in_last_month": 20, "views": 90},

    # Home Appliances
    {"id": 16, "category_id": 4, "item_name": "Blender", "price": 49.99, "number_of_left_in_stock": 20, "number_of_purchases_in_last_month": 15, "views": 60},
    {"id": 17, "category_id": 4, "item_name": "Microwave", "price": 99.99, "number_of_left_in_stock": 25, "number_of_purchases_in_last_month": 12, "views": 80},
    {"id": 18, "category_id": 4, "item_name": "Vacuum Cleaner", "price": 129.99, "number_of_left_in_stock": 30, "number_of_purchases_in_last_month": 10, "views": 50},
    {"id": 19, "category_id": 4, "item_name": "Air Fryer", "price": 149.99, "number_of_left_in_stock": 35, "number_of_purchases_in_last_month": 8, "views": 40},
    {"id": 20, "category_id": 4, "item_name": "Refrigerator", "price": 799.99, "number_of_left_in_stock": 10, "number_of_purchases_in_last_month": 5, "views": 30},

    # Beauty Products
    {"id": 21, "category_id": 5, "item_name": "Lipstick", "price": 9.99, "number_of_left_in_stock": 300, "number_of_purchases_in_last_month": 90, "views": 400},
    {"id": 22, "category_id": 5, "item_name": "Foundation", "price": 19.99, "number_of_left_in_stock": 200, "number_of_purchases_in_last_month": 50, "views": 300},
    {"id": 23, "category_id": 5, "item_name": "Eyeliner", "price": 7.99, "number_of_left_in_stock": 150, "number_of_purchases_in_last_month": 60, "views": 250},
    {"id": 24, "category_id": 5, "item_name": "Blush", "price": 12.99, "number_of_left_in_stock": 180, "number_of_purchases_in_last_month": 40, "views": 200},
    {"id": 25, "category_id": 5, "item_name": "Face Serum", "price": 29.99, "number_of_left_in_stock": 100, "number_of_purchases_in_last_month": 25, "views": 150}
]
    for data in items_data:

        Item.objects.create(id=data['id'], category_id=data['category_id'], item_name=data['item_name'], price=data['price'], \
                             number_of_left_in_stock=data['number_of_left_in_stock'], number_of_purchases_in_last_month=\
                                data['number_of_purchases_in_last_month'], views=data['views'])
        
def create_property():

    property_data = [
    {"id": 1, "property_name": "Color"},
    {"id": 2, "property_name": "Brand"},
    {"id": 3, "property_name": "Screen Size"},
    {"id": 4, "property_name": "Material"},
    {"id": 5, "property_name": "Weight"},
    {"id": 6, "property_name": "Author"},
    {"id": 7, "property_name": "Publisher"},
    {"id": 8, "property_name": "Dimensions"},
    {"id": 9, "property_name": "Type"},
    {"id": 10, "property_name": "Volume"}
]
    for data in property_data:

        Property.objects.create(id=data['id'], property_name=data['property_name'])

def create_item_property():

    item_property_data = [
    # Electronics
    {"id": 1, "item_id": 1, "property_id": 1, "value": "Black"},
    {"id": 2, "item_id": 1, "property_id": 2, "value": "Samsung"},
    {"id": 3, "item_id": 1, "property_id": 3, "value": "6.4 inches"},
    {"id": 4, "item_id": 1, "property_id": 5, "value": "0.4 lbs"},

    {"id": 5, "item_id": 2, "property_id": 1, "value": "Silver"},
    {"id": 6, "item_id": 2, "property_id": 2, "value": "Dell"},
    {"id": 7, "item_id": 2, "property_id": 3, "value": "15.6 inches"},
    {"id": 8, "item_id": 2, "property_id": 5, "value": "4.5 lbs"},

    {"id": 9, "item_id": 3, "property_id": 1, "value": "White"},
    {"id": 10, "item_id": 3, "property_id": 2, "value": "Apple"},
    {"id": 11, "item_id": 3, "property_id": 3, "value": "44mm"},
    {"id": 12, "item_id": 3, "property_id": 5, "value": "1.1 lbs"},

    {"id": 13, "item_id": 4, "property_id": 1, "value": "Blue"},
    {"id": 14, "item_id": 4, "property_id": 2, "value": "Sony"},
    {"id": 15, "item_id": 4, "property_id": 3, "value": "2.5 inches"},
    {"id": 16, "item_id": 4, "property_id": 5, "value": "0.3 lbs"},

    {"id": 17, "item_id": 5, "property_id": 1, "value": "Grey"},
    {"id": 18, "item_id": 5, "property_id": 2, "value": "Lenovo"},
    {"id": 19, "item_id": 5, "property_id": 3, "value": "10.1 inches"},
    {"id": 20, "item_id": 5, "property_id": 5, "value": "1.2 lbs"},

    # Books
    {"id": 21, "item_id": 6, "property_id": 6, "value": "Author A"},
    {"id": 22, "item_id": 6, "property_id": 7, "value": "Publisher X"},
    {"id": 23, "item_id": 6, "property_id": 8, "value": "6x9 inches"},
    {"id": 24, "item_id": 6, "property_id": 9, "value": "Paperback"},

    {"id": 25, "item_id": 7, "property_id": 6, "value": "Author B"},
    {"id": 26, "item_id": 7, "property_id": 7, "value": "Publisher Y"},
    {"id": 27, "item_id": 7, "property_id": 8, "value": "7x10 inches"},
    {"id": 28, "item_id": 7, "property_id": 9, "value": "Hardcover"},

    # Clothing
    {"id": 29, "item_id": 11, "property_id": 1, "value": "Red"},
    {"id": 30, "item_id": 11, "property_id": 4, "value": "Cotton"},
    {"id": 31, "item_id": 11, "property_id": 8, "value": "M, L, XL"},

    {"id": 32, "item_id": 12, "property_id": 1, "value": "Blue"},
    {"id": 33, "item_id": 12, "property_id": 4, "value": "Denim"},
    {"id": 34, "item_id": 12, "property_id": 8, "value": "30, 32, 34, 36"},

    # Home Appliances
    {"id": 35, "item_id": 16, "property_id": 2, "value": "Philips"},
    {"id": 36, "item_id": 16, "property_id": 9, "value": "Electric"},
    {"id": 37, "item_id": 16, "property_id": 10, "value": "1.5L"},

    # Beauty Products
    {"id": 38, "item_id": 21, "property_id": 1, "value": "Pink"},
    {"id": 39, "item_id": 21, "property_id": 9, "value": "Matte"},
    {"id": 40, "item_id": 21, "property_id": 10, "value": "0.3 oz"}
]
    for data in item_property_data:

        ItemProperty.objects.create(id=data['id'], item_id=data['item_id'], property_id=data['property_id'], value=data['value'])