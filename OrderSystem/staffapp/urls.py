# staffapp/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # staffappのメニュー画面 (例: /staff/menu/)
    path('menu/', views.menu, name='staff_menu'),

    # staffappの一覧表示画面
    path('sh/', views.show, name='staff_show'),
    # staffappの登録入力画面
    path('in/', views.InputView.as_view(), name='staff_in'),
    # staffappの登録確認画面
    path('ico/', views.IConfirmView.as_view(), name='staff_ico'),
    # staffappの登録完了画面
    path('ire/', views.IResultView.as_view(), name='staff_ire'),
]
