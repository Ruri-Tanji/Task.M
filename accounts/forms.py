from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Account

#form class
class AccountForm(forms.ModelForm):
    #password
    password = forms.CharField(widget=forms.PasswordInput(), label="パスワード")

    class Meta():
        #ユーザー認証
        model = User
        #フィールド指定
        fields = ('username', 'email', 'password')
        #フィールド名指定
        labels = {'username': "ユーザID", 'email': "メールアドレス"}