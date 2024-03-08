from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'bg-[#1a202e] text-slate-300 rounded-xl outline-none focus:ring-1 ring-solid focus:ring-[#C0392B] text-sm font-light py-3 px-4 w-full', 
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-[#1a202e] text-slate-300 rounded-xl outline-none focus:ring-1 ring-solid focus:ring-[#C0392B] text-sm font-light py-3 px-4 w-full', 
        'placeholder': 'Password'
    }))
