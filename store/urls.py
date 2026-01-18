from django.urls import path
from .views import index, about_view, product_list, product_detail, product_add, product_edit 

urlpatterns = [
    path('', index, name='index'),
    path('about/', about_view, name='about'),
    path('products/', product_list, name='product_list'),
    path('products/add/', product_add, name='product_add'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('products/<int:product_id>/edit/', product_edit, name='product_edit'),
]