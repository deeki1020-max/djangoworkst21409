
#TODO 例題6 Fromクラスを継承したGoodsFormクラスの作成
#入力フィールドはBootstrapで装飾します
#3種類の入力部品を利用します
#CLASSIFY_CATEGORY_CHOICESという名前で選択項目を作成Dします。項目は健康飲料、定番飲料、アルコール
#BUYER_CATEGORY_CHOICEという名前で選択項目を作成します。項目は2101,渡部商事,2102,丸井物産,2103,佐賀商事
#文字入力のgoods_code列の生成、ラベルは商品名コード
#文字入力のgoods_name列の生成、ラベルは商品名
#リスト選択のclassify列の生成、ラベルは分類、選択項目はCLASSIFY_CATEGORY_CHOICE
#数値入力のsl_price列の生成、ラベル売上単価、最小値0、最大値1000
#数値入力のcs_price列の生成、ラベル仕入単価、最小値0、最大値1000
#数値入力のstock列の生成、ラベル在庫数、最小値0、最大値1000
#リスト選択のbuy_code列の生成、ラベルは仕入先コード、選択項目はBUYER_CATEGORY_CHOICE

# * 入力部品を作る場合には、〇〇Formという名前のクラスを利用
# * Djangoで用意されている機能を利用する⇒継承

from django import forms

from .models import Goods

# 分類選択肢 (クラスの外に定義するのが一般的です)
CLASSIFY_CATEGORY_CHOICES = [
    ('', '---------'), # 空の選択肢を追加
    ('健康飲料', '健康飲料'),
    ('定番飲料', '定番飲料'),
    ('アルコール', 'アルコール'),
]


# Goodsモデルに対応するフォーム
class GoodsForm(forms.ModelForm):

    class Meta:
        model = Goods
        fields = [
            'goods_code',
            'goods_name',
            'classify',
            'sl_price',
            'cs_price',
            'stocks',
            'buy_code',
        ]
        labels = {
            'goods_code': '商品コード',
            'goods_name': '商品名',
            'classify': '分類',
            'sl_price': '売上単価',
            'cs_price': '仕入単価',
            'stocks': '在庫数',
            'buy_code': '仕入先コード',
        }
        widgets = {
            'goods_code': forms.TextInput(),
            'goods_name': forms.TextInput(),
            'classify': forms.Select(choices=CLASSIFY_CATEGORY_CHOICES),
            'sl_price': forms.NumberInput(),
            'cs_price': forms.NumberInput(),
            'stocks': forms.NumberInput(),
            'buy_code': forms.Select(), # choicesは __init__ で設定
        }

    # 初期化処理専用の関数(入力画面生成時に実行する関数)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # すべてのフィールドにBootstrapデザインを適用
        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

        # 仕入先コードの選択肢をBuyerモデルから動的に生成
        # 循環インポートを避けるため、メソッド内でインポートします
        from buyerapp.models import Buyer
        self.fields['buy_code'].widget.choices = [('', '---------')] + [
            (buyer.buy_code, buyer.buy_name) for buyer in Buyer.objects.all()
        ]
        # もしインスタンス(編集対象のデータ)があれば、それは編集フォーム
        if self.instance and self.instance.pk:
            # 商品コードを読み取り専用にする
            self.fields['goods_code'].widget.attrs['readonly'] = 'readonly'
