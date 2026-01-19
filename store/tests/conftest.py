import pytest
from store.models import Category, Product
from decimal import Decimal


@pytest.fixture
def category_kpop():
    return Category.objects.create(
        name="Альбомы K-pop", description="Корейские поп-альбомы"
    )


@pytest.fixture
def category_merch():
    return Category.objects.create(
        name="Мерч Blackpink", description="Официальный мерч Blackpink"
    )


@pytest.fixture
def blackpink_album(category_kpop):
    return Product.objects.create(
        name="THE ALBUM",
        description="Первый студийный альбом BLACKPINK",
        price=Decimal("2999.99"),
        category=category_kpop,
    )


@pytest.fixture
def born_pink_album(category_kpop):
    return Product.objects.create(
        name="BORN PINK",
        description="Второй студийный альбом",
        price=Decimal("3499.99"),
        category=category_kpop,
    )
