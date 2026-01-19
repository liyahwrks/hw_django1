import pytest
from decimal import Decimal
from store.models import Category, Product


@pytest.mark.django_db
def test_category_creation():
    """Создание категории"""
    category = Category.objects.create(name="Синглы", description="Синглы Blackpink")

    assert Category.objects.count() == 1
    assert category.name == "Синглы"
    assert str(category) == "Синглы"


@pytest.mark.django_db
def test_product_creation(category_kpop):
    """Создание товара"""
    album = Product.objects.create(
        name="KILL THIS LOVE",
        description="Мини-альбом 2019",
        price=Decimal("2499.99"),
        category=category_kpop,
    )

    assert Product.objects.count() == 1
    assert album.name == "KILL THIS LOVE"
    assert album.price == Decimal("2499.99")
    assert album.category.name == "Альбомы K-pop"
    assert str(album) == "KILL THIS LOVE"


@pytest.mark.django_db
def test_product_update(blackpink_album):
    """Обновление товара"""
    blackpink_album.price = Decimal("1999.99")
    blackpink_album.save()

    updated = Product.objects.get(pk=blackpink_album.pk)
    assert updated.price == Decimal("1999.99")
