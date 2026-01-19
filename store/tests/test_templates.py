import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_product_list_template(client, blackpink_album, born_pink_album):
    """Тест шаблона"""
    url = reverse("product_list")
    response = client.get(url)

    assert response.status_code == 200

    content = response.content.decode()

    assert "THE ALBUM" in content
    assert "BORN PINK" in content
