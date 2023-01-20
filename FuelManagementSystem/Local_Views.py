from django.shortcuts import render, redirect
from app.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Avg, Count, Min, Sum


def HOME(request):
    employee = Employee.objects.filter(admin=request.user.id)
    print(employee)
    for i in employee:
        employee_id = i.id
        print(employee_id)
        employee_coupon = FuelExpense.objects.filter(employee_id=employee_id)

        context = {
            "employee_coupon": employee_coupon
        }

        return render(request, "Local/view_coupon.html", context)


def ADD_COUPON(request, id):
    employee = Employee.objects.filter(id=id)
    petrolpump = Petrolpump.objects.all()
    fueltype = FuelType.objects.all()
    fiscal_year = FiscalYear.objects.all()
    context = {
        "employee": employee,
        "petrolpump": petrolpump,
        "fueltype": fueltype,
        "fiscal_year": fiscal_year,
    }

    return render(request, 'Local/add_coupon.html', context)


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


def VIEW_COUPON(request):
    employee = Employee.objects.filter(admin=request.user.id)
    print(employee)
    for i in employee:
        employee_id = i.id
        employee_coupon = FuelExpense.objects.filter(employee_id=employee_id)

        context = {
            "employee_coupon": employee_coupon
        }

        return render(request, "Local/view_coupon.html", context)


def STAFF_ADD_COUPON(request):

    employee = Employee.objects.filter(admin=request.user.id)

    print(employee)
    petrolpump = Petrolpump.objects.all()
    fueltype = FuelType.objects.all()
    fiscal_year = FiscalYear.objects.all()
    context = {
        "employee": employee,
        "petrolpump": petrolpump,
        "fueltype": fueltype,
        "fiscal_year": fiscal_year,
    }
    return render(request, 'Local/ask_coupon.html', context)


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
        messages.success(request, 'Your request has been sent')
        return redirect('view_staff_coupon')

    return render(request, 'Local/view_staff_coupon.html')


'''def LOCAL_APPLY_VISIT(request):

    person = Person.objects.filter(admin=request.user.id)
    for i in person:
        person_id = i.id
        person_leave_history = Local_Apply_Visit.objects.filter(
            person_id=person_id)
        context = {
            'person_leave_history': person_leave_history
        }

        return render(request, 'Local/apply_visit.html', context)
'''

'''def LOCAL_APPLY_VISIT_SAVE(request):
    if request.method == "POST":
        document = request.FILES.get('document')
        country = request.POST.get('country')
        purpose = request.POST.get('purpose')
        sponser = request.POST.get('sponser')
        visit_start_date = request.POST.get('visit_start_date')
        visit_end_date = request.POST.get('visit_end_date')
        visitor = request.POST.get('visitor')
        person = Person.objects.get(admin=request.user.id)
        visit = Local_Apply_Visit(
            person_id=person,
            country_visit=country,
            purpose_visit=purpose,
            sponser=sponser,
            from_date=visit_start_date,
            to_date=visit_end_date,
            visitors=visitor,
            document=document,

        )
        visit.save()
        messages.success(request, 'Your application sent successfully')
        return redirect('local_apply_visit')

'''
'''def VIEW(request):
    person_id = Person.objects.get(admin=request.user.id)
    context = {
        "person_id": person_id

    }

    return render(request, 'Local/view_local_level.html', context)
'''
