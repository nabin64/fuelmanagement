from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *

# from app.models import Course, Session_Year, CustomUser, Student, Staff, Subject,
from django.contrib import messages
from django.db.models import Avg, Count, Min, Sum


def HOME(request):
    employee_count = Employee.objects.all().count()
    petrolpump_count = Petrolpump.objects.all().count()
    disel = FuelExpense.objects.filter(
        fueltype='1').aggregate(disel_consume_sum=Sum('liter'))
    disel_consume = disel['disel_consume_sum']

    petrol = FuelExpense.objects.filter(
        fueltype='2').aggregate(petrol_consume_sum=Sum('liter'))
    petrol_consume = petrol['petrol_consume_sum']

    fuel = FuelExpense.objects.all().order_by('-id')[0:5]

    context = {
        "disel_consume": disel_consume,
        "employee_count": employee_count,
        "petrolpump_count": petrolpump_count,
        "petrol_consume": petrol_consume,
        "fuel": fuel



    }

    return render(request, "Hod/home.html", context)


def PRINT_COUPON_HOME(request):
    employee_count = Employee.objects.all().count()
    petrolpump_count = Petrolpump.objects.all().count()
    disel = FuelExpense.objects.filter(
        fueltype='1').aggregate(disel_consume_sum=Sum('liter'))
    disel_consume = disel['disel_consume_sum']

    petrol = FuelExpense.objects.filter(
        fueltype='2').aggregate(petrol_consume_sum=Sum('liter'))
    petrol_consume = petrol['petrol_consume_sum']

    fuel = FuelExpense.objects.all().order_by('-id')[0:5]

    context = {
        "disel_consume": disel_consume,
        "employee_count": employee_count,
        "petrolpump_count": petrolpump_count,
        "petrol_consume": petrol_consume,
        "fuel": fuel



    }

    return render(request, "Hod/home.html", context)


def ADD_EMPLOYEE(request):
    department = Department.objects.all()
    workplace = WorkPlace.objects.all()
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        appointed_date = request.POST.get('appointed_date')
        name = request.POST.get('name')
        workplace = request.POST.get('workplace')
        dep_name_id = request.POST.get('dep_name')
        designation = request.POST.get('designation')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        vehicle = request.POST.get('vehicle')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=name,
                username=username,

                email=email,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()

            department = Department.objects.get(id=dep_name_id)
            workplace = WorkPlace.objects.get(id=workplace)

            employee = Employee(
                admin=user,
                appointed_date=appointed_date,
                name=name,
                workplace=workplace,
                department=department,
                designation=designation,
                mobile=mobile,
                email=email,
                vehicle=vehicle,



            )
            employee.save()
            messages.success(request, user.first_name + "  " +
                             "Are Successfully Added !")
            return redirect('view_employee')

    context = {
        "department": department,
        "workplace": workplace,
    }
    return render(request, 'Hod/add_employee.html', context)


def VIEW_EMPLOYEE(request):
    employee = Employee.objects.all()
    context = {
        "employee": employee
    }
    return render(request, "Hod/view_employee.html", context)


def EDIT_EMPLOYEE(request, id):
    employee = Employee.objects.filter(id=id)
    department = Department.objects.all()
    workplace = WorkPlace.objects.all()
    context = {
        "employee": employee,
        "department": department,
        "workplace": workplace,
    }
    return render(request, 'Hod/edit_employee.html', context)


def UPDATE_EMPLOYEE(request):

    if request.method == "POST":
        workplace_id = request.POST.get('workplace')
        department_id = request.POST.get('dep_name')
        employee_id = request.POST.get('employee_id')
        profile_pic = request.FILES.get('profile_pic')
        appointed_date = request.POST.get('appointed_date')
        name = request.POST.get('name')

        designation = request.POST.get('designation')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        vehicle = request.POST.get('vehicle')
        user = CustomUser.objects.get(id=employee_id)

        user.first_name = name
        user.email = email
        user.username = username

        if profile_pic != None and profile_pic != '':
            user.profile_pic = profile_pic

        if password != None and password != '':
            user.set_password(password)
        user.save()

        employee = Employee.objects.get(admin=employee_id)
        employee.appointed_date = appointed_date
        employee.name = name
        employee.email = email

        employee.designation = designation
        employee.mobile = mobile
        employee.vehicle = vehicle

        workplace = WorkPlace.objects.get(id=workplace_id)
        department = Department.objects.get(id=department_id)
        employee.workplace_id = workplace
        employee.department_id = department
        employee.save()
        messages.success(request, 'Records are successfully updated')
        return redirect('view_employee')

    return render(request, 'Hod/edit_employee.html')


def VIEW_DEPARTMENT(request):
    department = Department.objects.all()
    context = {
        "department": department
    }
    return render(request, "Hod/view_department.html", context)


def VIEW_PETROLPUMP(request):
    petrolpump = Petrolpump.objects.all()
    context = {
        "petrolpump": petrolpump
    }
    return render(request, "Hod/view_petrolpump.html", context)


def ADD_DEPARTMENT(request):
    department = Department.objects.all().order_by('-id')[0:5]
    context = {
        "department": department
    }

    if request.method == "POST":
        dep_name = request.POST.get('dep_name')

        department = Department(
            dep_name=dep_name
        )
        department.save()
        return redirect("add_department")

    return render(request, 'hod/add_department.html', context)


def ADD_PETROLPUMP(request):
    petrolpump = Petrolpump.objects.all()
    context = {
        "petrolpump": petrolpump
    }

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=name,
                username=username,
                email=email,
                user_type=3
            )
            user.set_password(password)
            user.save()
            petrolpump = Petrolpump(
                name=name,
                address=address,
                contact=contact,
            )
            petrolpump.save()
            messages.success(request, "Petorlpump added successfully ")
            return redirect('add_petrolpump')

    return render(request, 'hod/add_petrolpump.html', context)


def ISSUE_COUPON(request):
    if request.method == "POST":
        fiscal_year_id = request.POST.get('fiscal_year')
        coupon_date = request.POST.get('date')
        employee_id = request.POST.get('employee_id')
        name = Employee.objects.get(admin=employee_id)

        petrolpump_id = request.POST.get('petrolpump_name')
        fuel_type_id = request.POST.get('fuel_type')
        liter = request.POST.get('liter')

        fiscal_year = FiscalYear.objects.get(id=fiscal_year_id)
        petrolpump = Petrolpump.objects.get(id=petrolpump_id)
        fuel_type = FuelType.objects.get(id=fuel_type_id)

        coupon = FuelExpense(
            employee=name,
            patrolpump=petrolpump,
            fueltype=fuel_type,
            liter=liter,
            date=coupon_date,
            fiscalyear=fiscal_year,

        )
        coupon.save()
        messages.success(request, 'Records are successfully Saved')
        return redirect('view_coupon')

    return render(request, 'Hod/view_coupon.html')


def PRINT_COUPON(request, id):
    coupon = FuelExpense.objects.get(id=id)
    context = {
        "coupon": coupon,
    }
    coupon.status = 1
    coupon.save()
    return render(request, 'Hod/print_coupon.html', context)


def VIEW_COUPON(request):
    coupon = FuelExpense.objects.all().order_by('-id')
    context = {
        "coupon": coupon
    }

    return render(request, 'Hod/view_coupon.html', context)


def REPORT_COUPON_EMPLOYEE(request, id):
    coupon = FuelExpense.objects.filter(employee=id)
    context = {
        "coupon": coupon
    }
    return render(request, "Hod/report_coupon.html", context)


def REPORT_COUPON_PETROLPUMP(request, id):
    coupon = FuelExpense.objects.filter(patrolpump=id)
    context = {
        "coupon": coupon
    }
    return render(request, "Hod/report_coupon.html", context)


def SEARCH_COUPON(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')

        coupon = FuelExpense.objects.filter(date__range=(
            fromdate, todate)) & FuelExpense.objects.filter(patrolpump=request.POST.get('name'))

        context = {
            "coupon": coupon
        }
        return render(request, 'Hod/search_coupon.html', context)

    coupon = FuelExpense.objects.all()
    patrolpump = Petrolpump.objects.all()
    context = {
        "coupon": coupon,
        "patrolpump": patrolpump,

    }
    return render(request, 'Hod/search_coupon.html', context)


def VIEW_REQUESTED_COUPON(request):
    coupon = FuelExpense.objects.filter(status='0')
    context = {
        "coupon": coupon
    }

    return render(request, 'Hod/view_request_coupon.html', context)


def SEARCH_COUPON_DATEWISE(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')

        coupon = FuelExpense.objects.filter(date__range=(fromdate, todate))

        context = {
            "coupon": coupon
        }
        return render(request, 'Hod/search_coupon_datewise.html', context)

    coupon = FuelExpense.objects.all()
    patrolpump = Petrolpump.objects.all()
    context = {
        "coupon": coupon,
        "patrolpump": patrolpump,

    }
    return render(request, 'Hod/search_coupon_datewise.html', context)
