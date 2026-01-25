from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.contrib import messages
from .models import Product, Category
from .forms import ProductModelForm
from .tasks import log_new_product


class IndexTemplateView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница !"
        return context


class AboutTemplateView(TemplateView):
    template_name = "store/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "О нас !"
        return context


class ProductBase:
    model = Product
    context_object_name = "product"


class ProductListView(ProductBase, ListView):
    template_name = "store/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get("category")
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Список товаров"
        return context


class ProductDetailView(ProductBase, DetailView):
    template_name = "store/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context


class ProductCreateView(ProductBase, CreateView):
    template_name = "store/product_form.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавить новый товар"
        return context

    def form_valid(self, form):
        product = form.save()

        log_new_product.delay(
            product_name=product.name,
            product_price=str(product.price),
        )

        messages.success(self.request, "Товар успешно создан")

        return super().form_valid(form)


class ProductUpdateView(ProductBase, UpdateView):
    template_name = "store/product_form.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Редактировать {self.object.name}"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Товар успешно обновлен")
        return super().form_valid(form)


class ProductDeleteView(ProductBase, DeleteView):
    template_name = "store/product_confirm_delete.html"
    success_url = reverse_lazy("product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Удалить {self.object.name}"
        return context
