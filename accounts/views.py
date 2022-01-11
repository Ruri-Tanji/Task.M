from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from .forms import AccountForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# ログイン
def Login(request):
    # Post
    if request.method =='POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            # ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'accounts/login.html')

# ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('login'))

# ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "todo/home.html", context=params)

# 新規登録
class AccountCreate(TemplateView):

    def __init__(self):
        self.params = {
            "AccountCreate":False,
            "account_form":AccountForm()
        }

    def get(self, request):
        self.params["account_form"] = AccountForm()
        self.params["AccountCreate"] = False
        return render(request, "accounts/accounts.html", context=self.params)

    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)

        if self.params["account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            self.params["AccountCreate"] = True

        else:
            # フォームが有効出ない場合
            print(self.params["account_form"].errors)

        return render(request, "accounts/accounts.html", context=self.params)