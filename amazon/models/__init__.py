from .user import User
from .address import Address
from .item import Item
from .itemproperty import ItemProperty
from .cart import Cart
from .order import Order
from .itemscart import ItemsCart
from .useraddress import UserAddress
from .category import Category
from .itemswhishlist import ItemsWhishlist
from .payment import Payment
from .whishlist import Whishlist
from .paymentmethod import PaymentMethod
from .property import Property
from .itemviews import ItemView
from .emi import Emi
from .itemwarranty import ItemWarranty
from .offer import Offer
from .warranty import Warranty
from .exchangeproperty import ExchangeProperty
from .itememi import ItemEmi
from .itemoffer import ItemOffer
from .itemexchangeproperty import ItemExchangeProperty
from .deliveryavailability import DeliveryAvailability
from .rating import Rating
from .exchangevalue import ExchangeValue
from .refund import Refund
from .orderitem import OrderItem

__all__ = [User, Address, Item, ItemProperty, Cart, Order, ItemsCart, UserAddress, Category, ItemsWhishlist, Payment, Whishlist, \
           PaymentMethod, Property, ItemView, Emi, ItemWarranty, Offer, Warranty, ExchangeProperty, ItemEmi, ItemOffer, \
            ItemExchangeProperty, DeliveryAvailability, Rating, ExchangeValue, Refund, OrderItem]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
