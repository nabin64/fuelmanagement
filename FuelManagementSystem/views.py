from django.shortcuts import render, redirect, HttpResponse
from app.models import *
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def HOME(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),)

        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('local_home')
            elif user_type == '3':
                return redirect('patrol_home')

            else:
                messages.error(request, "Email and Password are Invalid")
                return redirect('login')
        else:
            messages.error(request, "Email and Password are Invalid")
            return redirect('login')

    return None


def doLogout(request):
    logout(request)
    return redirect('login')


def LOAD_DISTRICT(request):
    province_id = request.GET.get('provinceid')

    district = District.objects.filter(province_id=province_id).all()

    context = {
        "district": district,
    }
    return render(request, 'Hod/district_drop_down.html', context)


def LOAD_LOCAL_LEVEL(request):
    district_id = request.GET.get('district_id')

    local_level = Local_Level.objects.filter(district_id=district_id).all()

    context = {
        "local_level": local_level
    }
    return render(request, 'Hod/local_level_drop_down.html', context)
