from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # staffappのURLをインクルード
    # 'staff/' で始まるURLへのアクセスを staffapp.urls に転送します。
    path('staff/', include('staffapp.urls')),
    # customerappのURLをインクルード
    path('customer/', include('customerapp.urls')),
    # buyerappのURLをインクルード
    path('buyer/', include('buyerapp.urls')),
    # goodsappのURLをインクルード
    path('goods/', include('goodsapp.urls')),
    # トップページ (ルートURL) の設定を追加
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
