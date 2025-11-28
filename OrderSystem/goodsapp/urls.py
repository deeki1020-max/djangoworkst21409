# goodsapp/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.menu, name='goods_menu'),
    path('sh/', views.show, name='goods_show'),
    path('in/', views.InputView.as_view(), name='goods_in'),
    path('ico/', views.IConfirmView.as_view(), name='goods_ico'),
    path('ire/', views.IResultView.as_view(), name='goods_ire'),

    # ★ここを <int:pk> から <str:pk> に変更
    path('ed/<str:pk>/', views.EditView.as_view(), name='goods_ed'),

    path('eco/', views.EConfirmView.as_view(), name='goods_eco'),
    path('ere/', views.EResultView.as_view(), name='goods_ere'),

    # 削除機能用のURLパターンを追加
    path('del/<str:pk>/', views.GoodsDeleteView.as_view(), name='goods_del'),
]
