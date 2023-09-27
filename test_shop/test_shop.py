"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from .models import Product, Cart


@pytest.fixture
def product():
    return Product("music plate", 250.55, "music plate with music Michael Jackson", 20)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1)
        assert product.check_quantity(20)
        assert product.check_quantity(0)
        assert product.check_quantity(200) is False
        assert product.check_quantity(-5) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(5)
        assert product.quantity == 15

        product.buy(0)
        assert product.quantity == 15

        product.buy(15)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(10000)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 10)
        assert cart.get_total_price() == 2505.5

    def test_buy_more_products_that_available(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()

    def test_buy_products(self, cart, product):
        cart.add_product(product, 15)
        cart.buy()
        assert product.quantity == 5

    def test_product_to_cart(self, cart, product):
        cart.add_product(product, 19)
        assert cart.products[product] == 19
        cart.add_product(product, 1)
        assert cart.products[product] == 20

    def test_delete_product_from_cart_more_then_in_cart(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 10)
        assert cart.products == {}

    def test_delete_product_from_cart_more_then_in_cart_no_quantity(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product)
        assert cart.products == {}

    def test_delete_product_that_in_cart(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 3)
        assert cart.products == {}

    def test_delete_product_from_cart(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 2)
        assert cart.products[product] == 1

    def test_clear_cart(self, cart, product):
        cart.add_product(product, 1)
        cart.clear()
        assert cart.products == {}

