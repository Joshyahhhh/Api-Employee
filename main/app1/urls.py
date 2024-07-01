from django.contrib import admin
from django.urls import path, include
from app1.views import (
    get_employees_from_api,
    employee_detail,
    employee_edit,
    employee_delete,
    employee_add
)


    
urlpatterns = [
    path("", get_employees_from_api, name='get_employees_from_api'),
    path('employee/<int:employee_id>/', employee_detail, name='employee_detail'),
    path('employee_edit/<int:employee_id>/', employee_edit, name='employee_edit'),
    path('employee_delete/<int:employee_id>/', employee_delete, name='employee_delete'),
    path('employee_add/', employee_add, name='employee_add'),
    path('admin/', admin.site.urls),
]