# customerapp/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # メニュー画面: 'customer/menu/'
    path('menu/', views.menu, name='customer_menu'),
    # 一覧表示画面: 'customer/sh/'
    path('sh/', views.show, name='customer_show'),
    # 登録入力画面: 'customer/in/'
    path('in/', views.InputView.as_view(), name='customer_in'),
    # 登録確認画面: 'customer/ico/'
    path('ico/', views.IConfirmView.as_view(), name='customer_ico'),
    # 登録完了画面: 'customer/ire/'
    path('ire/', views.IResultView.as_view(), name='customer_ire'),
]
