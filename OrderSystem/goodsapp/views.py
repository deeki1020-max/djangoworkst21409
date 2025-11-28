from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, View

from .forms import GoodsForm
from .models import Goods


# Create your views here.
#TODO 例題5 menu関数の作成
# goodsappのメニュー画面を表示する関数
def menu(request):
    return render(request, 'goodsapp/menu.html')

# 商品情報一覧を表示する関数
def show(request):
    """
    データベースに登録されているすべての商品情報を取得し、
    一覧表示画面をレンダリングします。
    """
    # Goodsモデルからすべてのオブジェクトを取得します
    goods_list = Goods.objects.all()
    # 取得した商品リストをテンプレートに渡します
    return render(request, 'goodsapp/show.html', {'goods_list': goods_list})
#TODO 例題１０ その２ CreateViewを使ったInputViewの作成

class InputView(CreateView):
    model = Goods
    form_class = GoodsForm
    template_name = 'goodsapp/input.html'
    success_url = reverse_lazy('goods_ico')

    def get_form(self, form_class=None):
        #セッションから初期データを取得
        initial_data = self.request.session.get('igoods_data', None)
        form = super().get_form(form_class)
        if initial_data:
            form.initial = initial_data
        return form
    def form_valid(self, form):
        #フォームデータが有効な場合、せっしょに保存
        self.request.session['igoods_data'] = form.cleaned_data
        return redirect(self.success_url)

class IConfirmView(View):
    # !GETリクエスト（画面表示）を処理する
    def get(self, request, *args, **kwargs):
        # セッションから 'igoods_data' を取得します
        igoods_data = request.session.get('igoods_data')
        # セッションデータがない場合は、入力画面にリダイレクトします
        if not igoods_data:
            return redirect('goods_in')
        # 取得したデータをテンプレートに渡して、確認画面を表示します
        return render(request, 'goodsapp/iconfirm.html', {'data': igoods_data})
    # !POSTリクエスト（確定ボタン押下）を処理する
    def post(self, request, *args, **kwargs):
        # セッションから 'igoods_data' を取得します
        igoods_data = request.session.get('igoods_data')
        # セッションデータがなければ入力画面に戻します
        if not igoods_data:
            return redirect('goods_in')
        # セッションのデータを使ってGoodsオブジェクトを作成し、DBに保存します
        Goods.objects.create(**igoods_data)
        # 完了画面へリダイレクトします
        return redirect('goods_ire')

# 商品登録の完了ビュー
class IResultView(View):
    def get(self, request, *args, **kwargs):
        # セッションから登録データを取得
        igoods_data = request.session.get('igoods_data', None)

        # 完了画面を表示したらセッションデータを削除します
        request.session.pop('igoods_data', None)

        # 'iresult.html' をレンダリングして、完了画面を表示します。
        return render(request, 'goodsapp/iresult.html', {'data': igoods_data})

# 商品編集の入力ビュー (UpdateViewを継承)
class EditView(UpdateView):
    model = Goods
    form_class = GoodsForm
    template_name = 'goodsapp/edit.html'
    # 編集確認画面のURL名を指定します
    success_url = reverse_lazy('goods_eco')

    def form_valid(self, form):
        # フォームの入力が正しい場合、データをセッションに保存します
        # セッションキーは命名規則に従い 'egoods_data' とします
        self.request.session['egoods_data'] = form.cleaned_data
        return redirect(self.get_success_url())

# 商品編集の確認ビュー
class EConfirmView(View):
    # GETリクエスト（画面表示）を処理する
    def get(self, request, *args, **kwargs):
        # セッションから 'egoods_data' を取得します
        egoods_data = request.session.get('egoods_data')
        # セッションデータがない場合は、一覧画面にリダイレクトします
        if not egoods_data:
            return redirect('goods_show')

        # 変更前のデータをDBから取得します
        original_goods = Goods.objects.get(pk=egoods_data['goods_code'])

        # テンプレートに「変更前」と「変更後」のデータを渡して表示します
        return render(request, 'goodsapp/econfirm.html', {
            'original_data': original_goods,
            'edited_data': egoods_data,
        })

    # POSTリクエスト（確定ボタン押下）を処理する
    def post(self, request, *args, **kwargs):
        # セッションから 'egoods_data' を取得します
        egoods_data = request.session.get('egoods_data')
        if not egoods_data:
            return redirect('goods_show')

        # 対象の商品データをDBから取得し、セッションのデータで上書きして保存します
        goods_to_update = Goods.objects.get(pk=egoods_data['goods_code'])
        form = GoodsForm(egoods_data, instance=goods_to_update)
        if form.is_valid():
            form.save()

        # 完了画面で表示するために、更新後のデータをセッションに保存します
        request.session['eugoods_data'] = egoods_data

        # 完了画面へリダイレクトします
        return redirect('goods_ere')

# 商品編集の完了ビュー
class EResultView(View):
    def get(self, request, *args, **kwargs):
        # セッションから更新後のデータを取得します
        eugoods_data = request.session.get('eugoods_data')

        # 完了画面を表示したら不要なセッションデータを削除します
        if 'egoods_data' in request.session:
            del request.session['egoods_data']
        if 'eugoods_data' in request.session:
            del request.session['eugoods_data']

        # 'eresult.html' をレンダリングして、完了画面を表示します
        return render(request, 'goodsapp/eresult.html', {'data': eugoods_data})

# 商品削除のビュー (DeleteViewを継承)
class GoodsDeleteView(DeleteView):
    # 対象のモデルを指定
    model = Goods
    # 削除確認画面のテンプレートを指定
    template_name = 'goodsapp/dconfirm.html'
    # 削除成功後にリダイレクトするURLを指定 (商品一覧画面)
    success_url = reverse_lazy('goods_show')

    # context_object_name を指定すると、テンプレートで 'object' の代わりに 'goods' を使えるようになります
    context_object_name = 'goods'
