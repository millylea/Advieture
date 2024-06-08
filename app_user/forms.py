from django import forms
from app_user.models import User


class FormRegister(forms.ModelForm):
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Họ"}),
    )

    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Tên"}),
    )

    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Tên đăng nhập"}
        ),
    )

    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Điện thoại"}
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )

    password = forms.CharField(
        max_length=250,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Mật khẩu"}
        ),
    )
    confirm_password = forms.CharField(
        max_length=250,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Xác nhận Mật khẩu"}
        ),
    )

    class Meta:
        model = User
        fields = "__all__"
