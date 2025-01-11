from amazon.models import User, Address, Item, ItemProperty, Cart, Order, ItemsCart, UserAddress, Category, ItemsWhishlist, Payment, Whishlist, \
              PaymentMethod, Property, ItemView, Emi, ItemWarranty, Offer, Warranty, ExchangeProperty, ItemEmi, ItemOffer, \
                ItemExchangeProperty, DeliveryAvailability, Rating, ExchangeValue
from amazon.interactors.item_interactors.item_performance_interactor import ItemPerformanceInteractor
from amazon.storages.storage_implementation import StorageImplementation
from amazon.presenters.presenter_implementation import PresenterImplementation

def populate_data():

  storage = StorageImplementation()
  presenter = PresenterImplementation()
  interactor = ItemPerformanceInteractor(storage=storage, presenter=presenter)
  items = interactor.get_list_best_selling_items()
  for item in items:
      print(item.item_id)
