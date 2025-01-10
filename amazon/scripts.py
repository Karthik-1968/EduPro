from amazon.models import User, Address, Item, ItemProperty, Cart, Order, ItemsCart, UserAddress, Category, ItemsWhishlist, Payment, Whishlist, \
              PaymentMethod, Property, ItemView, Emi, ItemWarranty, Offer, Warranty, ExchangeProperty, ItemEmi, ItemOffer, \
                ItemExchangeProperty, DeliveryAvailability, Rating, ExchangeValue
from amazon.interactors.whichlist_interactor import WhichListInteractor
from amazon.storages.storage_implementation import StorageImplementation
from amazon.presenters.presenter_implementation import PresenterImplementation

def populate_data():

  storage = StorageImplementation()
  presenter = PresenterImplementation()
  interactor = WhichListInteractor(storage=storage, presenter=presenter)
  items = interactor.get_recommendations_for_user(user_id="a68d063f-3723-43dd-8dee-3b7a62665c01")

  print(items)
