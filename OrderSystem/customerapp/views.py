from django.shortcuts import redirect, render
from django.views import View

from .forms import CustomerForm
from .models import Customer


# customerappのメニュー画面を表示する関数
def menu(request):
    """
    得意先管理機能のメニュー画面をレンダリングして表示します。
    """
    return render(request, 'customerapp/menu.html')

# 得意先情報一覧を表示する関数
def show(request):
    """
    データベースに登録されているすべての得意先情報を取得し、
    一覧表示画面をレンダリングします。
    """
    # Customerモデルからすべてのオブジェクトを取得します
    customer_list = Customer.objects.all()
    # 取得した得意先リストをテンプレートに渡します
    return render(request, 'customerapp/show.html', {'customer_list': customer_list})

# --- 以下、登録機能用のビュー（仮実装） ---

class InputView(View):
    def get(self, request, *args, **kwargs):
        initial_data = request.session.get('icustomer_data', None)
        form = CustomerForm(initial=initial_data)
        return render(request, 'customerapp/input.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomerForm(request.POST)
        if form.is_valid():
            request.session['icustomer_data'] = form.cleaned_data
            return redirect('customer_ico')
        return render(request, 'customerapp/input.html', {'form': form})

class IConfirmView(View):
    def get(self, request, *args, **kwargs):
        customer_data = request.session.get('icustomer_data')
        if not customer_data:
            return redirect('customer_in')
        return render(request, 'customerapp/iconfirm.html', {'data': customer_data})

    def post(self, request, *args, **kwargs):
        customer_data = request.session.get('icustomer_data')
        if not customer_data:
            return redirect('customer_in')
        Customer.objects.create(**customer_data)
        return redirect('customer_ire')

class IResultView(View):
    def get(self, request, *args, **kwargs):
        # セッションから登録データを取得します
        customer_data = request.session.get('icustomer_data', None)
        # 完了画面を表示したらセッションデータを削除します
        if 'icustomer_data' in request.session:
            del request.session['icustomer_data']
        # 'iresult.html' をレンダリングして、完了画面を表示します
        return render(request, 'customerapp/iresult.html', {'data': customer_data})
