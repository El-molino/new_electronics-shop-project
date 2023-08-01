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

def test_item_name():
    item1 = Item("Телевизор", 10000, 20)
    item2 = Item("УльтрахдТелевизор", 10000, 20)
    assert item1.name == "Телевизор"
    assert item2.name == "Ультрахдтелевизор"
    assert print(item2.name) == print("Наименования товара должно быть не больше 10 симвовов")


def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert len(items) == 5

    item1 = items[0]
    assert item1.name == 'Смартфон'
    assert item1.price == 100
    assert item1.quantity == 1


def test_string_to_number():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5