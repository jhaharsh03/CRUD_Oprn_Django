from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Home Page
    path('', views.home, name='home'),

    # Path to Add an Employee
    path('add_employee', views.add_employee, name='add_employee'),
    # Path to View Employee in details
    path('employee/<str:employee_id>', views.employee, name='employee'),
    # Path to Delete an Employee
    path('delete_employee/<str:employee_id>', views.delete_employee, name='delete_employee'),
    # Path to edit an Employee
    path('edit_employee', views.edit_employee, name='edit_employee'),
]