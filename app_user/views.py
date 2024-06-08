from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime
from app_travel.models import Category, Tour
from app_user.models import User
from app_user.forms import FormRegister

salt = "123456"
hasher = PBKDF2PasswordHasher()


# Create your views here.
def register(request):
    categories = Category.objects.all()
    form_register = FormRegister()
    result_register = ""
    if request.POST.get("btnRegister"):
        form_register = FormRegister(request.POST, User)
        if form_register.is_valid():
            if (
                form_register.cleaned_data["password"]
                == form_register.cleaned_data["confirm_password"]
            ):
                request.POST._mutable = True
                post = form_register.save(commit=False)
                post.first_name = form_register.cleaned_data["first_name"]
                post.last_name = form_register.cleaned_data["last_name"]
                post.username = form_register.cleaned_data["username"]
                post.phone = form_register.cleaned_data["phone"]
                post.email = form_register.cleaned_data["email"]
                post.password = hasher.encode(
                    form_register.cleaned_data["password"], salt
                )
                post.confirm_password = form_register.cleaned_data["confirm_password"]
                post.save()
                result_register = """
                <div class="alert alert-success" role="alert">
                        Đăng Ký Tài Khoản Thành Công!
                </div> """
                return redirect("app_travel:login")
            else:
                result_register = """
                <div class="alert alert-danger" role="alert">
                        Thông tin có lỗi, vui lòng nhập lại!
                </div> """
    return render(
        request,
        "app_travel/register.html",
        {
            "result_register": result_register,
            "form_register": form_register,
            "categories": categories,
        },
    )


def login(request):
    categories = Category.objects.all()
    result_login = ""
    if request.POST.get("btnDangnhap"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        password = hasher.encode(password, salt)
        user = User.objects.filter(username=username, password=password)
        if user.count() > 0:
            dict_user = user.values().first()
            request.session["s_user"] = dict_user
            return redirect("app_travel:index")
        else:
            result_login = """
                <div class="alert alert-danger" role="alert">
                        Mật khẩu và Tên đăng nhập không trùng khớp!
                </div> """
    return render(
        request,
        "app_travel/log-in.html",
        {
            "result_login": result_login,
            "categories": categories,
        },
    )


def logout(request):
    if "s_user" in request.session:
        del request.session["s_user"]
        return redirect("app_user:login")


def my_account(request):
    categories = Category.objects.all()
    dict_user = request.session["s_user"]
    user = User.objects.get(pk=request.session["s_user"]["id"])

    if not "s_user" in request.session:
        return redirect("app_travel:login")

    result_update = ""
    if request.POST.get("btnUpdate"):
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        # put into database
        user.last_name = last_name
        user.first_name = first_name
        user.phone = phone
        user.email = email
        user.address = address
        user.save()
        # put into session
        dict_user["last_name"] = last_name
        dict_user["first_name"] = first_name
        dict_user["phone"] = phone
        dict_user["email"] = email
        dict_user["address"] = address

        result_update = """
                <div class="alert alert-success" role="alert">
                        Thông tin đã được cập nhật
                </div> """

    result_password = ""
    if request.POST.get("btnChangePassword"):
        password = request.POST.get("password")
        if user.password == password:
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")
            if new_password == confirm_password:
                user.password = hasher.encode(new_password, salt)
                user.save()
                result_password = """
                <div class="alert alert-success" role="alert">
                        Mật khẩu đã được cập nhật
                </div> """
            else:
                result_password = """
                <div class="alert alert-danger" role="alert">
                        mật khẩu không khớp!
                </div> """
        else:
            result_password = """
                <div class="alert alert-danger" role="alert">
                        sai mật khẩu!
                </div> """
    return render(
        request,
        "app_travel/my-account.html",
        {
            "user": user,
            "categories": categories,
            "result_update": result_update,
            "result_password": result_password,
        },
    )
