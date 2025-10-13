from django import forms
from .models import Product
from django.core.exceptions import ValidationError
import os


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price_product', 'product_category', 'product_picture', 'product_description']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'введите название продукта'
        })

        self.fields['price_product'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'введите цену продукта'
        })

        self.fields['product_category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'введите категорию продукта'
        })

        self.fields['product_picture'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['product_description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'введите описание продукта'
        })

    def clean_product_picture(self):
        file = self.cleaned_data.get('product_picture')
        valid_extensions = ['.jpeg', '.png', ]
        ext = os.path.splitext(file.name)[1].lower()
        if ext not in valid_extensions:
            raise ValidationError('Поддерживаются только следующие форматы: JPEG, PNG')
        if file.size > 5*1024*1024:
            raise ValidationError('Размер файла не должен превышать 5 Мб')
        return file

    def clean_price_product(self):
        price = self.cleaned_data.get('price_product')
        if int(price) < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price


    def clean(self):
        cleaned_data = super().clean()
        product_name = cleaned_data.get('product_name')
        description = cleaned_data.get('product_description')
        stop_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        flag_name = False
        flag_description = False
        for i in stop_list:
            if i in product_name.lower():
                flag_name = True
        for i in stop_list:
            if i in description.lower():
                flag_description = True

        if product_name and flag_name:
            self.add_error('product_name', 'Name не может содержать запрещенное слово')
        if description and flag_description:
            self.add_error('product_description', 'Описание не может содержать запрещенное слово')
