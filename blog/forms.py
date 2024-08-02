from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'video']


from django import forms
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm, PasswordChangeForm as AuthPasswordChangeForm
from django.contrib.auth.models import User

class CustomUserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
        }

class CustomPasswordChangeForm(AuthPasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور فعلی'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور جدید'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور جدید'}))

    class Meta:
        model = User
        fields = []
