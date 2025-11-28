from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from .forms import BuyerForm
# Buyerモデルと、これから作成するBuyerFormをインポートします
from .models import Buyer


# buyerappのトップページ用の仮のビュー
def index(request):
    # トップページはメニュー画面にリダイレクトするのが一般的です
    return redirect('buyer_menu')

# buyerappのメニュー画面を表示する関数
def menu(request):
    return render(request, 'buyerapp/menu.html')

# 仕入先情報一覧を表示する関数
def show(request):
    """
    データベースに登録されているすべての仕入先情報を取得し、
    一覧表示画面をレンダリングします。
    """
    # Buyerモデルからすべてのオブジェクトを取得します
    buyer_list = Buyer.objects.all()
    # 取得した仕入先リストをテンプレートに渡します
    return render(request, 'buyerapp/show.html', {'buyer_list': buyer_list})

# 仕入先登録の入力ビュー (CreateViewを継承)
class InputView(CreateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'buyerapp/input.html'
    # 登録確認画面のURL名を指定します
    success_url = reverse_lazy('buyer_ico')

    def form_valid(self, form):
        # フォームの入力が正しい場合、データをセッションに保存します
        # セッションキーは命名規則に従い 'ibuyer_data' とします
        self.request.session['ibuyer_data'] = form.cleaned_data
        return redirect(self.success_url)

# 仕入先登録の確認ビュー
class IConfirmView(View):
    # GETリクエスト（画面表示）を処理する
    def get(self, request, *args, **kwargs):
        # セッションから 'ibuyer_data' を取得します
        ibuyer_data = request.session.get('ibuyer_data')
        # セッションデータがない場合は、入力画面にリダイレクトします
        if not ibuyer_data:
            return redirect('buyer_in')
        # 取得したデータをテンプレートに渡して、確認画面を表示します
        return render(request, 'buyerapp/iconfirm.html', {'data': ibuyer_data})

    # POSTリクエスト（確定ボタン押下）を処理する
    def post(self, request, *args, **kwargs):
        # セッションから 'ibuyer_data' を取得します
        ibuyer_data = request.session.get('ibuyer_data')
        # セッションデータがなければ入力画面に戻します
        if not ibuyer_data:
            return redirect('buyer_in')
        # セッションのデータを使ってBuyerオブジェクトを作成し、DBに保存します
        Buyer.objects.create(**ibuyer_data)
        # 完了画面へリダイレクトします
        return redirect('buyer_ire')

# 仕入先登録の完了ビュー
class IResultView(View):
    def get(self, request, *args, **kwargs):
        # セッションから登録データを取得します
        ibuyer_data = request.session.get('ibuyer_data', None)
        # 完了画面を表示したらセッションデータを削除します
        if 'ibuyer_data' in request.session:
            del request.session['ibuyer_data']
        # 'iresult.html' をレンダリングして、完了画面を表示します
        return render(request, 'buyerapp/iresult.html', {'data': ibuyer_data})
