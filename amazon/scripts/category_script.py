from amazon.models import Category

def create_category():

    category_data=[
    {"id": 1, "category_name": "Electronics"},
    {"id": 2, "category_name": "Books"},
    {"id": 3, "category_name": "Clothing"},
    {"id": 4, "category_name": "Home Appliances"},
    {"id": 5, "category_name": "Beauty Products"}
]
    for data in category_data:

        Category.objects.create(id=data['id'], category_name=data['category_name'])
