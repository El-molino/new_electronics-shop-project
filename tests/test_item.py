"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

pay_rate = 0.85


@pytest.fixture
def test_item():
    return Item("Телевизор", 80000, 5)


def test_init(test_item):
    assert test_item.name == "Телевизор"
    assert test_item.price == 80000
    assert test_item.quantity == 5


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 400000


def test_apply_discount(test_item):
    assert test_item.apply_discount() is None
    "так и не понял как протестировать скидку"
