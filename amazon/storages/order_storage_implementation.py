from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.interactors.storage_interfaces.dtos import OrderItemDTO, OrderCartItemsDTO
from amazon.models import Order, OrderItem, ItemsCart
from amazon.exceptions import order_custom_exceptions

class OrderStorageImplementation(OrderStorageInterface):

    def create_order_for_item(self, orderitem_dto:OrderItemDTO)->int:

        order = Order.objects.create(
            user_id=orderitem_dto.user_id,
            address_id=orderitem_dto.address_id,
            order_status=orderitem_dto.order_status,
            delivary_date=orderitem_dto.delivary_date
        )

        orderitem = OrderItem.objects.create(order_id=order.id, item_id=orderitem_dto.item_id)

        for item_property in orderitem_dto.item_properties:
            orderitem.add(item_property)

        return order.id
    
    def create_order_for_cart(self, ordercartitems_dto:OrderCartItemsDTO)->int:

        order = Order.objects.create(
            user_id=ordercartitems_dto.user_id,
            address_id=ordercartitems_dto.address_id,
            order_status=ordercartitems_dto.order_status,
            delivary_date=ordercartitems_dto.delivary_date
        )

        for item in ordercartitems_dto.item_ids:
            ordercartitem = OrderItem.objects.create(order_id=order.id, item_id=ordercartitems_dto.item_id)
            item_properties = ItemsCart.objects.get(id=ordercartitems_dto.cart_id, item_id=ordercartitems_dto.item_id).itemproperties.all()
            for item_property in item_properties:
                ordercartitem.add(item_property)

        return order.id
    
    def check_if_order_exists(self, order_id:int):

        order = Order.objects.filter(id=order_id).exists()
        order_not_exists = not order

        if order_not_exists:
            raise order_custom_exceptions.OrderDoesNotExistException(order_id=order_id)