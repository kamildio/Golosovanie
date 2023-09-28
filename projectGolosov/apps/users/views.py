from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, CustomUserForm
from .models import CustomUser
from django.db.models import Q


def signUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация произошла успешно!")
            return redirect("users:loginPage")
        messages.error(request, "При регистрации произошла ошибка")
    else:
        form = NewUserForm()
    return render(request, "users/sign-up.html", {
        'form': form
    })

def edit_user(request, user_id):
    user = CustomUser.objects.get(pk=user_id)

    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('golosApp:home')  # Замените 'profile' на URL, куда вы хотите перенаправить пользователя после успешного сохранения
    else:
        form = CustomUserForm(instance=user)

    return render(request, 'users/user-edit.html', {'form': form})


def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Добро пожаловать, {username}!")
                return redirect("golosApp:home")
            else:
                messages.error(request, "При входе произошла ошибка.")
        else:
            messages.error(request, "При входе произошла ошибка.")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {
        'form': form
    })


def logoutUser(request):
    logout(request)
    messages.info(request, "Вы вышли из аккаунта.")
    return redirect("golosApp:home")

def profilePage(request, user_id):
    profile = CustomUser.objects.get(pk=user_id)
    return render(request, "users/user-profile.html", {
        'profile': profile
    })