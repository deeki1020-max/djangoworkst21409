# buyerapp/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # メニュー画面: 'buyer/menu/'
    path('menu/', views.menu, name='buyer_menu'),
    # 一覧表示画面: 'buyer/sh/'
    path('sh/', views.show, name='buyer_show'),
    # 登録入力画面: 'buyer/in/'
    path('in/', views.InputView.as_view(), name='buyer_in'),
    # 登録確認画面: 'buyer/ico/'
    path('ico/', views.IConfirmView.as_view(), name='buyer_ico'),
    # 登録完了画面: 'buyer/ire/'
    path('ire/', views.IResultView.as_view(), name='buyer_ire'),
]
