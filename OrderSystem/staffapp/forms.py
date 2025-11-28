from django import forms
from django.core.validators import (MaxValueValidator,  # ★ここを追加
                                    MinValueValidator)

from .models import Staff


# Staffモデルに対応するフォーム
class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = ['staff_code', 'staff_name', 'work_years', 'wages']
        labels = {
            'staff_code': '社員コード',
            'staff_name': '社員名',
            'work_years': '勤続年数',
            'wages': '給与',
        }

    def __init__(self, *args, **kwargs):
        """
        フォームの初期化メソッドです。
        すべてのフィールドにBootstrapの 'form-control' クラスを自動的に適用します。
        """
        super().__init__(*args, **kwargs)

        # すべての入力項目を Bootstrap の form-control に
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        # 各フィールドのバリデーションルールを個別に設定
        self.fields['staff_code'].validators.append(
            MinValueValidator(0)
        )

        self.fields['work_years'].validators.extend([
            MinValueValidator(0),
            MaxValueValidator(100),
        ])

        self.fields['wages'].validators.extend([
            MinValueValidator(0),
            MaxValueValidator(1_000_0000),  # 10000000 と同じ
        ])
