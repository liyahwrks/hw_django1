import pytest
from decimal import Decimal
from store.forms import ProductModelForm
from store.models import Category


@pytest.mark.django_db
def test_valid_product_form(category_kpop):
    """Валидация формы"""
    form_data = {
        "name": "THE ALBUM DELUXE",
        "description": "Расширенное издание",
        "price": "3999.99",
        "category": category_kpop.id,
    }

    form = ProductModelForm(data=form_data)
    assert form.is_valid() == True
