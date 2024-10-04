from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request,'all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=first_name,
                           last_name=last_name,
                           salary=salary,
                           bonus=bonus,
                           dept=dept,
                           role=role,
                           hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee Added Successfully !')
    elif request.method == 'GET':
        departments = Department.objects.all()
        roles = Role.objects.all()
        return render(request,'add_emp.html',{'departments': departments, 'roles': roles})
    else:
        return HttpResponse('An Exception Occurred ! Employee hHas Not Been Added !')
    
    
def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully !")
        except:
            return HttpResponse('Please Enter A Valid Employee ID')
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        emps = Employee.objects.all()
        if name :
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept :
            emps = emps.filter(dept__id = dept)
        if role :
            emps = emps.filter(role__id = role)
        context = {
            'emps' : emps
        }
        return render(request, 'all_emp.html',context)
    
    elif request.method == 'GET' :
        departments = Department.objects.all()
        roles = Role.objects.all()
        return render(request,'filter_emp.html',{'departments': departments, 'roles': roles})
        
    else:
        return HttpResponse('An Exception Occurred.')