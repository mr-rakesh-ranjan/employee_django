from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Employee

# Create your views here.

def emp_home(request):
    emps=Employee.objects.all()
    return render(request, 'emp_tamplates/home.html', {
        'emps':emps
    })

def add_employee(request):
    if request.method == 'POST':
        # fetching data from form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        employee_email = request.POST.get('employee_email')
        employee_phone = request.POST.get('employee_phone')
        employee_department = request.POST.get('employee_department')
        employee_address = request.POST.get('employee_address')
        newsletter_checked = request.POST.get('newsletter_checked')

        # create a model
        e=Employee()
        e.first_name=first_name
        e.last_name=last_name
        e.email=employee_email
        e.phone=employee_phone
        e.department=employee_department
        e.address=employee_address
        if newsletter_checked  is None:
            e.emp_isActive = False
        else:
            e.emp_isActive = True
        print("data is comming")

        # save data to db
        e.save()
        return redirect('/emp/home/')
    return render(request, 'emp_tamplates/add_employee.html', {})

def delete_employee(request, emp_id):
    # print(emp_id)  #for debugging purpose
    employee = Employee.objects.get(pk=emp_id)
    employee.delete()
    return redirect('/emp/home/')

def update_employee(request, emp_id):
    employee=Employee.objects.get(pk=emp_id)
    return render(request, 'emp_tamplates/update_employee.html', {
        'employee':employee
    })

def do_update_employee(request,emp_id):
    if request.method == 'POST':
        # fetching data from form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        employee_email = request.POST.get('employee_email')
        employee_phone = request.POST.get('employee_phone')
        employee_department = request.POST.get('employee_department')
        employee_address = request.POST.get('employee_address')
        newsletter_checked = request.POST.get('newsletter_checked')

        e = Employee.objects.get(pk=emp_id)

        e.first_name=first_name
        e.last_name=last_name
        e.email=employee_email
        e.phone=employee_phone
        e.department=employee_department
        e.address=employee_address
        if newsletter_checked  is None:
            e.emp_isActive = False
        else:
            e.emp_isActive = True

        e.save()
        return redirect('/emp/home/')
