from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.storage_interfaces.dtos import ItemDTO, ItemsCartDTO, ItemIdDTO, RatingDTO
from amazon.models import Item, Property, ItemProperty, Cart, ItemsCart, Whishlist, ItemsWhishlist, Order, ItemView, Rating
from amazon.exceptions import item_custom_exceptions

class ItemStorageImplementation(ItemStorageInterface):

    def check_if_item_already_exists(self, item_name):

        if Item.objects.filter(name=item_name).exists():
            raise item_custom_exceptions.ItemAlreadyExistsException()
        
    def create_item(self, item_dto:ItemDTO)->int:
        
        item = Item.objects.create(item_name=item_dto.item_name, category_id=item_dto.category_id, price=item_dto.price, \
                                   number_of_left_in_stock=item_dto.number_of_left_in_stock, \
                                       number_of_purchases_in_last_month=item_dto.number_of_purchases_in_last_month)
        
        return item.id
    
    def check_if_property_already_exists(self, property_name:str):
        
        if Property.objects.filter(property_name=property_name).exists():
            raise item_custom_exceptions.PropertyAlreadyExistsException()
    
    def create_property(self, property_name:str)->int:

        property = Property.objects.create(
            property_name=property_name
        )

        return property.id
    
    def check_if_item_exists(self, item_id:int):

        item = Item.objects.filter(id=item_id).exists()
        item_not_exists = not item

        if item_not_exists:
            raise item_custom_exceptions.ItemDoesNotExistException(item_id=item_id)
        
    def check_if_property_exists(self, property_id:int):
        
        property = Property.objects.filter(id=property_id).exists()
        property_not_exists = not property

        if property_not_exists:
            raise item_custom_exceptions.PropertyDoesNotExistException(property_id=property_id)
        
    def add_property_to_item(self, item_id:int, property_id:int, value:str):

        itemproperty = ItemProperty.objects.create(
            item_id=item_id,
            property_id=property_id,
            value=value
        )

        return itemproperty.id
    
    def get_list_of_items(self)->list[ItemDTO]:
        
        items = Item.objects.all()
        item_dtos = []

        for item in items:
            item_dto = self._convert_item_object_to_dto(item)
            item_dtos.append(item_dto)
        
        return item_dtos
    
    def _convert_item_object_to_dto(item)->ItemDTO:
        
        item_dto = ItemDTO(
            item_name=item.name,
            category_id=item.category_id,
            price=item.price,
            number_of_left_in_stock=item.number_of_left_in_stock,
            number_of_purchases_in_last_month=item.number_of_purchases_in_last_month
        )

        return item_dto
    
    def get_list_of_items_by_category(self, category_id:int)->list[ItemDTO]:
        
        items = Item.objects.filter(category_id=category_id)
        item_dtos = []

        for item in items:
            item_dto = self._convert_item_object_to_dto(item)
            item_dtos.append(item_dto)
        
        return item_dtos
    
    def check_if_cart_already_created_for_user(self, user_id):
        
        if Cart.objects.filter(user_id=user_id).exists():
            raise custom_exceptions.CartAlreadyExistsException()
        
    def create_cart(self, user_id:str, name:str)->int:
        
        cart = Cart.objects.create(
            user_id=user_id, name=name
        )

        return cart.id
    
    def check_if_cart_exists(self, cart_id:int):
        
        cart = Cart.objects.filter(id=cart_id).exists()
        cart_not_exists = not cart

        if cart_not_exists:
            raise item_custom_exceptions.CartDoesNotExistException(cart_id=cart_id)
    
    def add_item_to_cart(self, itemscart_dto:ItemsCartDTO):
        
        itemscart = ItemsCart.objects.create(
            cart_id=itemscart_dto.cart_id,
            item_id=itemscart_dto.item_id
        )

        for item_property in itemscart_dto.item_properties:
            itemscart.add(item_property)

     def check_if_whishlist_already_created_for_user(self, user_id:str):
        
        if Whishlist.objects.filter(user_id=user_id).exists():
            raise item_custom_exceptions.WhishlistAlreadyCreatedException()
        
    def create_whishlist_for_user(self, user_id:str, name:str)->int:

        whishlist = Whishlist.objects.create(
            user_id=user_id,
            name=name
        )

        return whishlist.id
    
    def check_if_whishlist_exists(self, whishlist_id:int):
        
        whishlist = Whishlist.objects.filter(id=whishlist_id).exists()
        whishlist_not_exists = not whishlist

        if whishlist_not_exists:
            raise item_custom_exceptions.WhishlistDoesNotExistException(whishlist_id=whishlist_id)

    def add_item_to_whishlist(self, whishlist_id:int, item_id:int, item_properties:list[int]):

        itemswhishlist = ItemsWhishlist.objects.create(
            whishlist_id=whishlist_id,
            item_id=item_id
        )

        for item_property in item_properties:
            itemswhishlist.add(item_property)

    
    def check_if_item_exists_in_whishlist(self, whishlist_id:int, item_id:int):
        
        itemswhishlist = ItemsWhishlist.objects.filter(whishlist_id=whishlist_id, item_id=item_id).exists()
        item_not_exists = not itemswhishlist

        if item_not_exists:
            raise item_custom_exceptions.ItemDoesNotExistInWhishlistException(item_id=item_id, whishlist_id=whishlist_id)
        
    def check_if_item_property_exists(self, item_property_id:int):

        itemproperty = ItemProperty.objects.filter(id=item_property_id).exists()
        itemproperty_not_exists = not itemproperty

        if itemproperty_not_exists:
            raise item_custom_exceptions.ItemPropertyDoesNotExistException(item_property_id=item_property_id)
        
    def check_if_item_properties_exists(self, item_properties:list[int]):
        
        for item_property in item_properties:
            self.check_if_item_property_exists(item_property)

    def get_recommendations_for_user(self, user_id:str)->list[int]:

        recommendations = []
        categories = []
        orders = Order.objects.filter(user_id=user_id)
        for order in orders:
            item = Item.objects.get(id=order.item_id)
            categories.append(item.category_id)
        
        cart = Cart.objects.get(user_id=user_id)
        itemsincart = ItemsCart.objects.filter(cart_id=cart.id)
        for itemincart in itemsincart:
            item = Item.objects.get(id=itemincart.item_id)
            categories.append(item.category_id)

        whishlist = Whishlist.objects.get(user_id=user_id)
        itemsinwhishlist = ItemsWhishlist.objects.filter(whishlist_id=whishlist.id)
        for iteminwhishlist in itemsinwhishlist:
            item = Item.objects.get(id=iteminwhishlist.item_id)
            categories.append(item.category_id)

        itemviews = ItemView.objects.filter(user_id=user_id).select_related('item').order_by('-views')
        for itemview in itemviews:
            categories.append(itemview.item.category_id)

        for category in categories:
            items = Item.objects.filter(category_id=category)
            for item in items:
                recommendations.append(item.id)

        unique_recommendations = list(set(recommendations))

        recommendations_dtos = []

        for item in unique_recommendations:
            item_id_dto = ItemIdDTO(
                item_id=item
            )
            recommendations_dtos.append(item_id_dto)
        return recommendations_dtos
    
    def get_item_details(self, item_id:int)->ItemDTO:

        item = Item.objects.get(id=item_id)
        item.views+=1
        item.save()
        item_dto = self._convert_item_object_to_dto(item)
        
        return item_dto
    
    def add_view_to_item(self, user_id:str, item_id:int):

        if ItemView.objects.filter(user_id=user_id, item_id=item_id).exists():
            itemview = ItemView.objects.get(user_id=user_id, item_id=item_id)
            itemview.views+=1
            itemview.save()
        else:
            ItemView.objects.create(user_id=user_id, item_id=item_id, views=1)

    def get_list_best_selling_items(self)->list[int]:
        
        items = Item.objects.all().order_by('-number_of_purchases_in_last_month')[:100]
        best_selling_items_dtos = []
        for item in items:
            item_id_dto = ItemIdDTO(
                item_id=item.id
            )
            best_selling_items_dtos.append(item_id_dto)

        return best_selling_items_dtos
    
    def get_list_of_top_rated_items(self)->list[ItemIdDTO]:
        
        top_rated_items_dtos = []
        items = Item.objects.annotate(avg_rating=Avg('ratings__rating')).order_by('-avg_rating')[:100]
        for item in items:
            item_id_dto = ItemIdDTO(
                item_id=item.id
            )
            top_rated_items_dtos.append(item_id_dto)
        
        return top_rated_items_dtos
    
    def check_if_user_viewed_any_item(self, user_id:str):

        itemview = ItemView.objects.filter(user_id=user_id).exists()
        itemview_not_exists = not itemview
        if itemview_not_exists:
            raise item_custom_exceptions.UserHasNotViewedAnyItemException(user_id=user_id)
    
    def get_recently_viewed_item_by_user(self, user_id:str)->int:

        item = ItemView.objects.filter(user_id=user_id).order_by('-viewed_at').values_list('item_id', flat=True)[:1]
        
        return item
    
    def rate_an_item(self, item_id:int, user_id:str, rating:str)->int:

        item_rating = Rating.objects.create(item_id=item_id, user_id=user_id, rating=rating)

        return item_rating.id
    
    def check_if_item_is_rated(self, item_id:int):

        item_rating = Rating.objects.filter(item_id=item_id).exists()
        item_rating_not_exists = not item_rating

        if item_rating_not_exists:
            raise item_custom_exceptions.ItemIsNotRatedException(item_id=item_id)

    def check_if_user_already_rated_item(self, item_id:int, user_id:str):

        item_rating = Rating.objects.filter(item_id=item_id, user_id=user_id).exists()
        item_rating_exists = item_rating

        if item_rating_exists:
            raise item_custom_exceptions.UserAlreadyRatedItemException(user_id=user_id, item_id=item_id)
        
    def get_ratings_of_an_item(self, item_id:int)->list[RatingDTO]:

        ratings = Rating.objects.filter(item_id=item_id)
        rating_dtos = []

        for rating in ratings:
            rating_dto = self._convert_rating_object_to_dto(rating)
            rating_dtos.append(rating_dto)
        
        return rating_dtos
    
    def _convert_rating_object_to_dto(rating)->RatingDTO:
        
        rating_dto = RatingDTO(
            user_id=rating.user_id,
            rating=rating.rating
        )

        return rating_dto
