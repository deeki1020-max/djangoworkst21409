# customerapp/forms.py
from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    """
    得意先 (Customer) モデル用の ModelForm です。
    """
    class Meta:
        model = Customer
        fields = ['cust_code', 'cust_name', 'staff_code']
        labels = {
            'cust_code': '得意先コード',
            'cust_name': '得意先名',
            'staff_code': '担当者コード',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
