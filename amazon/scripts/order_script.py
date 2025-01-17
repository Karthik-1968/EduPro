from amazon.models import Order
from amazon.models import OrderItem

def create_order():

    order_data = {
        "user_id": "44ba532c-40a1-46da-8528-2e395576c131",
        "address_id": 2,
        "order_status": "Pending",
        "delivery_date": "2025-01-19T14:00:00",
        "item_id": 1,
        "is_in_cart": False,
        "itemproperties": [1, 2],
    }

    order = Order.objects.create(user_id=order_data['user_id'], address_id=order_data['address_id'], order_status=order_data['order_status'], delivery_date=order_data['delivery_date'])

    order_item = OrderItem.objects.create(order_id=order.id, item_id=order_data['item_id'], is_in_cart=order_data['is_in_cart'])

    for itemproperty in order_data['itemproperties']:
        order_item.itemproperties.add(itemproperty)
