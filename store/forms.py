from django import forms
from django.core.exceptions import ValidationError
from .models import Product, Category


class ProductForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label='Название товара',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название товара'})
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Введите описание товара'})
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Цена',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите цену'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Цена должна быть больше 0')
        return price

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise ValidationError('Название должно быть не менее 3 символов')
        return name


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'price')
        labels = {
            'name': 'Название товара',
            'category': 'Категория',
            'description': 'Описание',
            'price': 'Цена',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Введите описание'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите цену'}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Цена должна быть больше 0')
        return price

    def clean(self):
        FORBIDDEN_WORDS = ['бесплатно', 'даром', 'халява']
        data = super().clean()
        name = data.get('name')
        description = data.get('description')

        if name:
            for word in FORBIDDEN_WORDS:
                if word in name.lower():
                    raise ValidationError(f'Название не должно содержать слово "{word}"')
        
        if description:
            for word in FORBIDDEN_WORDS:
                if word in description.lower():
                    raise ValidationError(f'Описание не должно содержать слово "{word}"')