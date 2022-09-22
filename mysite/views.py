import re
from django.http import HttpResponse
from django.shortcuts import render
import datetime
def home(request):

    # Access data from user or url(request)

    # client_name = request.GET['name'] # when method is GET
    client_name=''
    # when method is 'POST'
    isActive=False
    if request.method=='POST':
        client_name=request.POST['client_name']
        check = request.POST.get('check')
        if check is None: 
            isActive=False
        else: isActive=True

    date = datetime.datetime.now()
    name=client_name
    list_of_program=[
        'WAP to check even or odd'
        'WAP tp check prime number'
        'The rabbit problem'
        'WAP to print all prime numbers from 1 tp 100'
        'WAP to print pascals triangle'
    ]

    student={
        'student_name':"Rakesh",
        'studnet_college':"RCCIIT",
        'student_city':"Kolkata",
    }

    data={
        'today_date':date,
        'isActive':isActive,
        'client_name':name,
        'list_of_program':list_of_program,
        'student_data': student

    }
    # return HttpResponse("<h1>Hello this is index page</h1>" + str(date))
    return render(request, "home.html", data)

def about(request):
    print("this is about page from views.py")
    # return HttpResponse("<h2>This is about page.</h2>")
    return render(request, "about.html", {})

def services(request):
    return render(request, "services.html", {}) 