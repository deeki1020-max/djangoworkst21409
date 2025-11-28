# staffapp/views.py

from django.shortcuts import redirect, render
from django.views import View

from .forms import StaffForm
from .models import Staff


# 社員管理メニュー画面を表示する関数
def menu(request):
    """
    社員管理機能のメニュー画面をレンダリングして表示します。
    """
    return render(request, 'staffapp/menu.html')

# 社員情報一覧を表示する関数
def show(request):
    """
    データベースに登録されているすべての社員情報を取得し、
    一覧表示画面をレンダリングします。
    """
    staff_list = Staff.objects.all()
    return render(request, 'staffapp/show.html', {'staff_list': staff_list})

# 社員情報登録の入力ビュー
class InputView(View):
    """
    社員情報の登録入力画面を扱うクラスベースビューです。
    GETリクエストで入力フォーム画面を表示し、
    POSTリクエストで入力内容を検証してセッションに保存します。
    """
    # GETリクエスト（画面表示）を処理するメソッド
    def get(self, request, *args, **kwargs):
        # セッションに 'istaff_data' があれば、それをフォームの初期値として設定します。
        # (例: 確認画面から「戻る」ボタンで戻ってきた場合など)
        initial_data = request.session.get('istaff_data', None)
        form = StaffForm(initial=initial_data)

        # 'input.html' をレンダリングして、フォームを画面に表示します。
        return render(request, 'staffapp/input.html', {'form': form})

    # POSTリクエスト（フォーム送信）を処理するメソッド
    def post(self, request, *args, **kwargs):
        # 送信されたデータ (request.POST) を使ってフォームを初期化します。
        form = StaffForm(request.POST)

        # is_valid() メソッドで、入力内容が正しいか (バリデーション) をチェックします。
        if form.is_valid():
            # バリデーションが通った場合、きれいになったデータ (cleaned_data) を
            # 'istaff_data' というキーでセッションに保存します。
            request.session['istaff_data'] = form.cleaned_data
            # 登録確認画面 ('ico') へリダイレクトします。
            return redirect('staff_ico')

        # バリデーションに失敗した場合、エラーメッセージが含まれたフォームを
        # 再度 'input.html' に渡して、入力画面を表示します。
        return render(request, 'staffapp/input.html', {'form': form})

# 社員登録の確認ビュー
class IConfirmView(View):
    # GETリクエスト（画面表示）を処理するメソッド
    def get(self, request, *args, **kwargs):
        # セッションから 'istaff_data' を取得します。
        staff_data = request.session.get('istaff_data')
        # セッションにデータがない場合は、入力画面へリダイレクトします。
        if not staff_data:
            return redirect('staff_in')

        # 取得したデータをテンプレートに渡して、確認画面を表示します。
        return render(request, 'staffapp/iconfirm.html', {'form_data': staff_data})

    # POSTリクエスト（確定ボタン押下）を処理するメソッド
    def post(self, request, *args, **kwargs):
        # セッションから 'istaff_data' を取得します。
        staff_data = request.session.get('istaff_data')
        # セッションデータがなければ入力画面に戻します。
        if not staff_data:
            return redirect('staff_in')

        # セッションのデータを使ってStaffオブジェクトを作成し、DBに保存します。
        Staff.objects.create(**staff_data)
        # 完了画面へリダイレクトします。
        return redirect('staff_ire')

# 社員登録の完了ビュー
class IResultView(View):
    # GETリクエスト（画面表示）を処理するメソッド
    def get(self, request, *args, **kwargs):
        # セッションから登録したデータを取得し、完了画面に渡します。
        istaff_data = request.session.get('istaff_data', None)

        # 完了画面を表示した後はセッションデータは不要なので削除します。
        if 'istaff_data' in request.session:
            del request.session['istaff_data']

        # 'iresult.html' をレンダリングして、完了画面を表示します。
        return render(request, 'staffapp/iresult.html', {'istaff_data': istaff_data})

#TODO例題10　確認画面から完了画面に変遷するとき
