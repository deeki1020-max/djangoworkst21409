# buyerapp/forms.py

from django import forms

from .models import Buyer


# Buyerモデルに対応するフォーム
class BuyerForm(forms.ModelForm):
    """
    仕入先 (Buyer) モデル用の ModelForm です。
    """

    def __init__(self, *args, **kwargs):
        """
        フォームの初期化メソッドです。
        すべてのフィールドにBootstrapの 'form-control' クラスを自動的に適用します。
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        # このフォームがどのモデルを対象にするかを指定します
        model = Buyer
        # フォームに表示するフィールドを指定します
        fields = ['buy_code', 'buy_name', 'staff_code']
        # フォームの各フィールドに表示するラベル名を指定します
        labels = {
            'buy_code': '仕入先コード',
            'buy_name': '仕入先名',
            'staff_code': '担当者コード',
        }
