from celery import shared_task
import time
from django.core.mail import send_mail


@shared_task
def log_new_product(product_name, product_price):
    """Задача для логирования нового товара"""
    message = f"Добавлен новый товар: {product_name} по цене {product_price} ₽"

    print(f"[CELERY TASK] {message}")

    send_mail(
        subject="Новый товар добавлен",
        message=message,
        from_email="admin@blackpink-shop.ru",
        recipient_list=["admin@example.com"],
    )

    return message
