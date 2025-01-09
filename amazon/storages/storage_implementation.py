from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.models import User, Address, UserAddress, Category, Item, Property, ItemProperty, Cart, ItemsCart, Order, Whishlist, \
    ItemsWhishlist, PaymentMethod, Payment, ItemView
from amazon.exceptions import custom_exceptions
from amazon.interactors.storage_interfaces.storage_interface import UserDTO, AddressDTO, CategoryDTO, ItemDTO, ItemsCartDTO,\
    OrderDTO, PaymentMethodDTO, OrderPaymentDTO

class StorageImplementation(StorageInterface):

    def check_if_user_already_exists(self, email:str, contact_number:str):
        
        if User.objects.filter(email=email).exists():
            raise custom_exceptions.UserAlreadyExistsException
        
        elif User.objects.filter(contact_number=contact_number).exists():
            raise custom_exceptions.UserAlreadyExistsException
        
    def create_user(self, user_dto:UserDTO)->str:

        user = User.objects.create(
            id=user_dto.id,
            name=user_dto.name,
            email=user_dto.email,
            contact_number=user_dto.contact_number,
        )

        return user.id
    
    def check_if_address_already_exists(self, address_dto:AddressDTO):

        if Address.objects.filter(door_no=address_dto.door_no, street=address_dto.street, city=address_dto.city, \
                                  district=address_dto.district, state=address_dto.state, country=address_dto.country, \
                                    pincode=address_dto.pincode, contact_number=address_dto.contact_number, \
                                        address_type=address_dto.address_type).exists():
            raise custom_exceptions.AddressAlreadyExistsException
        
    def create_address(self, address_dto:AddressDTO)->int:

        address = Address.objects.create(
            id=address_dto.id,
            door_no=address_dto.door_no,
            street=address_dto.street,
            city=address_dto.city,
            district=address_dto.district,
            state=address_dto.state,
            country=address_dto.country,
            pincode=address_dto.pincode,
            contact_number=address_dto.contact_number,
            address_type=address_dto.address_type
        )

        return address.id
    
    def check_if_user_exists(self, user_id:str):

        user = User.objects.filter(id=user_id).exists()
        user_not_exists = not user
        if user_not_exists:
            raise custom_exceptions.UserDoesNotExistException
        
    def check_if_address_exists(self, address_id:int):

        address = Address.objects.filter(id=address_id).exists()
        address_not_exists = not address
        if address_not_exists:
            raise custom_exceptions.AddressDoesNotExistException
        
    def check_if_address_already_added_to_user(self, user_id:str, address_id:int):

        if UserAddress.objects.filter(user_id=user_id, address_id=address_id).exists():
            raise custom_exceptions.AddressAlreadyAddedToUserException
        
    def add_address_to_user(self, user_id:str, address_id:int):
        
        UserAddress.objects.create(
            user_id=user_id,
            address_id=address_id
        )

    def check_if_category_already_exists(self, category_name):
        
        if Category.objects.filter(name=category_name).exists():
            raise custom_exceptions.CategoryAlreadyExistsException

    def create_category(self, category_name:str)->int:
        
        category = Category.objects.create(
            name=category_name
        )

        return category.id

    def get_list_of_categories(self)->list[CategoryDTO]:
        
        categories = Category.objects.all()
        category_dtos = []

        for category in categories:
            category_dto = self._convert_category_object_to_dto(category)
            category_dtos.append(category_dto)
        
        return category_dtos
    
    def _convert_category_object_to_dto(category)->CategoryDTO:
        
        category_dto = CategoryDTO(
            category_name=category.name
        )

        return category_dto
    
    def check_if_category_exists(self, category_id):
        
        category = Category.objects.filter(id=category_id).exists()
        category_not_exists = not category

        if category_not_exists:
            raise custom_exceptions.CategoryDoesNotExistException
        
    def check_if_item_already_exists(self, item_name):

        if Item.objects.filter(name=item_name).exists():
            raise custom_exceptions.ItemAlreadyExistsException
        
    def create_item(self, item_dto:ItemDTO)->int:
        
        item = Item.objects.create(item_name=item_dto.item_name, category_id=item_dto.category_id, price=item_dto.price, \
                                   number_of_left_in_stock=item_dto.number_of_left_in_stock, \
                                       number_of_purchases_in_last_month=item_dto.number_of_purchases_in_last_month)
        
        return item.id
    
    def check_if_property_already_exists(self, property_name:str):
        
        if Property.objects.filter(property_name=property_name).exists():
            raise custom_exceptions.PropertyAlreadyExistsException
    
    def create_property(self, property_name:str)->int:

        property = Property.objects.create(
            property_name=property_name
        )

        return property.id
    
    def check_if_item_exists(self, item_id:int):

        item = Item.objects.filter(id=item_id).exists()
        item_not_exists = not item

        if item_not_exists:
            raise custom_exceptions.ItemDoesNotExistException
        
    def check_if_property_exists(self, property_id:int):
        
        property = Property.objects.filter(id=property_id).exists()
        property_not_exists = not property

        if property_not_exists:
            raise custom_exceptions.PropertyDoesNotExistException()
        
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
            raise custom_exceptions.CartAlreadyExistsException
        
    def create_cart(self, user_id:str, name:str)->int:
        
        cart = Cart.objects.create(
            user_id=user_id, name=name
        )

        return cart.id
    
    def check_if_cart_exists(self, cart_id:int):
        
        cart = Cart.objects.filter(id=cart_id).exists()
        cart_not_exists = not cart

        if cart_not_exists:
            raise custom_exceptions.CartDoesNotExistException
    
    def add_item_to_cart(self, itemscart_dto:ItemsCartDTO):
        
        itemscart = ItemsCart.objects.create(
            cart_id=itemscart_dto.cart_id,
            item_id=itemscart_dto.item_id
        )

        for item_property in itemscart_dto.item_properties:
            itemscart.add(item_property)

    
    def create_order_for_item(self, order_dto:OrderDTO)->int:

        order = Order.objects.create(
            user_id=order_dto.user_id,
            item_id=order_dto.item_id,
            address_id=order_dto.address_id,
            order_status=order_dto.order_status
            delivary_date=order_dto.delivary_date
        )

        for item_property in order_dto.item_properties:
            order.add(item_property)

        return order.id
    
    def get_orders_of_user(self, user_id:str)->list[OrderDTO]:
        
        orders = Order.objects.filter(user_id=user_id)
        order_dtos = []

        for order in orders:
            order_dto = self._convert_order_object_to_dto(order)
            order_dtos.append(order_dto)
        
        return order_dtos
    
    def _convert_order_object_to_dto(order)->OrderDTO:

        order_dto = OrderDTO(
            user_id=order.user_id,
            item_id=order.item_id,
            address_id=order.address_id,
            order_status=order.order_status,
            delivary_date=order.delivary_date
        )

        return order_dto
    
    def check_if_whishlist_already_created_for_user(self, user_id:str):
        
        if Whishlist.objects.filter(user_id=user_id).exists():
            raise custom_exceptions.WhishlistAlreadyCreatedException
        
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
            raise custom_exceptions.WhishlistDoesNotExistException

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
            raise custom_exceptions.ItemDoesNotExistInWhishlistException
        
    def check_if_item_property_exists(self, item_property_id:int):

        itemproperty = ItemProperty.objects.filter(id=item_property_id).exists()
        itemproperty_not_exists = not itemproperty

        if itemproperty_not_exists:
            raise custom_exceptions.ItemPropertyDoesNotExistException
        
    def check_if_item_properties_exists(self, item_properties:list[int]):
        
        for item_property in item_properties:
            self.check_if_item_property_exists(item_property)

    def create_card_payment_method(self, paymentmethod_dto:PaymentMethodDTO)->int:
        
        paymentmethod = PaymentMethod.objects.create(
            payment_type=paymentmethod_dto.payment_type,
            card_name=paymentmethod_dto.card_name,
            card_number=paymentmethod_dto.card_number,
            card_holder_name=paymentmethod_dto.card_holder_name,
            cvv=paymentmethod_dto.cvv,
            expiry_date=paymentmethod_dto.expiry_date
            card_type=paymentmethod_dto.card_type
        )

        return paymentmethod.id
    

    def create_net_banking_payment_method(self, paymentmethod_dto:PaymentMethodDTO)->int:
        
        paymentmethod = PaymentMethod.objects.create(
            payment_type=paymentmethod_dto.payment_type,
            bank_name=paymentmethod_dto.bank_name,
            username=paymentmethod_dto.username,
            password=paymentmethod_dto.password
        )

        return paymentmethod.id
    

    def create_upi_payment_method(self, paymentmethod_dto:PaymentMethodDTO)->int:

        paymentmethod = PaymentMethod.objects.create(
            payment_type=paymentmethod_dto.payment_type,
            upi_id=paymentmethod_dto.upi_id
        )

        return paymentmethod.id
    
    def create_cash_on_delivery_payment_method(self, paymentmethod_dto:PaymentMethodDTO)->int:

        paymentmethod = PaymentMethod.objects.create(
            payment_type=paymentmethod_dto.payment_type
        )

        return paymentmethod.id
    
    def check_if_card_payment_method_already_exists(self, paymentmethod_dto:PaymentMethodDTO):

        if PaymentMethod.objects.filter(payment_type=paymentmethod_dto.payment_type, card_name=paymentmethod_dto.card_name,\
                                        card_number=paymentmethod_dto.card_number, \
                                         card_holder_name=paymentmethod_dto.card_holder_name, \
                                             cvv=paymentmethod_dto.cvv, expiry_date=paymentmethod_dto.expiry_date, \
                                                 card_type=paymentmethod_dto.card_type).exists():
            raise custom_exceptions.PaymentMethodAlreadyExistsException
        
    def check_if_net_banking_payment_method_already_exists(self, paymentmethod_dto:PaymentMethodDTO):

        if PaymentMethod.objects.filter(payment_type=paymentmethod_dto.payment_type, bank_name=paymentmethod_dto.bank_name, \
                                        username=paymentmethod_dto.username, password=paymentmethod_dto.password).exists():
            raise custom_exceptions.PaymentMethodAlreadyExistsException
        
    def check_if_upi_payment_method_already_exists(self, paymentmethod_dto:PaymentMethodDTO):

        if PaymentMethod.objects.filter(payment_type=paymentmethod_dto.payment_type, upi_id=paymentmethod_dto.upi_id).exists():
            raise custom_exceptions.PaymentMethodAlreadyExistsException
        
    def check_if_cash_on_delivery_payment_method_already_exists(self, paymentmethod_dto:PaymentMethodDTO):

        if PaymentMethod.objects.filter(payment_type=paymentmethod_dto.payment_type).exists():
            raise custom_exceptions.PaymentMethodAlreadyExistsException
        
    def check_if_order_exists(self, order_id:int):
        
        order = Order.objects.filter(id=order_id).exists()
        order_not_exists = not order

        if order_not_exists:
            raise custom_exceptions.OrderDoesNotExistException
        
    def check_if_payment_method_exists(self, payment_method_id:int):

        paymentmethod = PaymentMethod.objects.filter(id=payment_method_id).exists()
        paymentmethod_not_exists = not paymentmethod

        if paymentmethod_not_exists:
            raise custom_exceptions.PaymentMethodDoesNotExistException
        
    def add_payment_method_to_order(self, orderpayment_dto:OrderPaymentDTO)->:
        
        payment = Payment.objects.create(
            order_id=orderpayment_dto.order_id,
            payment_method_id=orderpayment_dto.payment_method_id,
            amount=orderpayment_dto.amount
            payment_status=orderpayment_dto.payment_status,
            transaction_id=orderpayment_dto.transaction_id
        )

        return payment.id
    
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

        return recommendations
    
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
        best_selling_items = []
        for item in items:
            best_selling_items.append(item.id)

        return best_selling_items
    
    def get_list_of_top_rated_items(self)->list[int]:
        
        items = Item.objects.all().order_by('-rating')[:100]
        top_rated_items = []
        for item in items:
            top_rated_items.append(item.id)

        return top_rated_items
    
    def check_if_user_viewed_any_item(self, user_id:str):

        itemview = ItemView.objects.filter(user_id=user_id).exists()
        itemview_not_exists = not itemview
        if itemview_not_exists:
            raise custom_exceptions.UserHasNotViewedAnyItemException
    
    def get_recently_viewed_item_by_user(self, user_id:str)->int:

        item = ItemView.objects.filter(user_id=user_id).order_by('-viewed_at').values_list('item_id', flat=True)[:1]
        
        return item