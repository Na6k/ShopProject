from decimal import Decimal
from django.conf import settings
from products.models import Products


class Cart:
    def __init__(self, request):  # инициализирую корзину
        self.session = request.session
        cart = self.session.get(settings.ORDER_SESSION_ID)
        if not cart:
            cart = self.session[
                settings.ORDER_SESSION_ID
            ] = {}  # save an empty cart in the session
        self.cart = cart

    def add(
        self, product, quantity=1, update_quantity=False
    ):  # Добавить продукт в корзину или обновить его количество.
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "price": str(product.price)}
        if update_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def save(self):
        self.session.modified = (
            True  # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        )

    def remove(self, product):  # Удаление товара из корзины.
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(
        self,
    ):  # Перебор элементов в корзине и получение продуктов из базы данных.
        product_ids = self.cart.keys()
        products = Products.objects.filter(
            id__in=product_ids
        )  # получение объектов product и добавление их в корзину
        for product in products:
            self.cart[str(product.id)]["products"] = product

        for item in self.cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):  # Подсчет всех товаров в корзине.
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):  # Подсчет стоимости товаров в корзине.
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

    def clear(self):  # удаление корзины из сессии
        del self.session[settings.ORDER_SESSION_ID]
        self.save()
