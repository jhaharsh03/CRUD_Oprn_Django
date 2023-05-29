from django.shortcuts import render
from App.models import Employee
from django.http import HttpResponseRedirect
from django.contrib import messages

# Function to render Homepage
def home(request):
    employee_list = Employee.objects.all()
    return render(request, 'home.html', {"employees": employee_list})

# Function to Add an Employee
def add_employee(request):
    if request.method == "POST":
        if (
            request.POST.get('name') and
            request.POST.get('email') and
            request.POST.get('occupation') and
            request.POST.get('salary') and
            request.POST.get('gender') or
            request.POST.get('note')
        ):
            employee = Employee()
            employee.name = request.POST.get('name')
            employee.email = request.POST.get('email')
            employee.occupation = request.POST.get('occupation')
            employee.salary = request.POST.get('salary')
            employee.gender = request.POST.get('gender')
            employee.note = request.POST.get('note')
            employee.save()
            messages.success(request, "Employee added successfully!")
            return HttpResponseRedirect("/")
    else:
        return render(request, "add.html")

# Function to View Employee in details
def employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if employee is not None:
        return render(request, "edit.html", {'employee': employee})

# Function to update an Employee
def edit_employee(request):
    if request.method == "POST":
        employee_id = request.POST.get('id')
        employee = Employee.objects.get(id=employee_id)
        if employee is not None:
            employee.name = request.POST.get('name')
            employee.email = request.POST.get('email')
            employee.occupation = request.POST.get('occupation')
            employee.salary = request.POST.get('salary')
            employee.gender = request.POST.get('gender')
            employee.note = request.POST.get('note')
            employee.save()
            messages.success(request, "Employee updated successfully!")
            return HttpResponseRedirect("/")

# Function to delete an Employee
def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    messages.success(request, "Employee deleted successfully!")
    return HttpResponseRedirect("/")

