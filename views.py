# authentication/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Parollar bir xil emas")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email allaqachon ro'yxatdan o'tgan")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu login allaqachon band")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz")
            return redirect('home')

        messages.error(request, "Noma'lum xatolik yuz berdi")
        return render(request, 'register.html')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username:
            messages.warning(request, "Loginni kiriting")
            return redirect('login')

        if not password:
            messages.warning(request, "Parolni kiriting")
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                logger.info(f"Admin {username} kirdi")
            auth_login(request, user)
            messages.success(request, "Xush kelibsiz")
            return redirect('home')
        else:
            logger.warning(f"Foydalanuvchi {username} kira olmadi")
            messages.error(request, "Username yoki parol xato")
            return redirect('login')

    return render(request, 'login.html')