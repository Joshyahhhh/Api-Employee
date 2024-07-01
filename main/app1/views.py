import json
import requests
from django.shortcuts import redirect, render
from .models import Employee
from django.http import HttpResponse, JsonResponse
from .forms import EmployeeForm

def get_employees_from_api(request):
    response = requests.get('https://joshya1234.pythonanywhere.com/api/Employee/?format=json')

    if response.status_code == 200:
        try:
            employees_data = response.json()
            for employee_data in employees_data.get('results'):
                employee, created = Employee.objects.get_or_create(
                    id=employee_data.get('id'),
                    defaults={
                        'name': employee_data.get('name'),
                        'salary': employee_data.get('salary'),
                        'age': employee_data.get('age'),
                        'image': employee_data.get('image')
                    }
                )
                if not created:
                    employee.name = employee_data.get('name')
                    employee.salary = employee_data.get('salary')
                    employee.age = employee_data.get('age')
                    employee.image = employee_data.get('image')
                employee.save()
                
            employees = Employee.objects.all()
            return render(request, 'app1/employees.html', {'employees': employees})
        except json.JSONDecodeError as e:
            return render(request, 'app1/error.html', {'error_message': 'Ошибка декодирования JSON данных из API'})
    else:
        return render(request, 'app1/error.html', 
            {'error_message': f'Не удалось получить данные из API. Код состояния: {response.status_code}'})
    

def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    return render(request, 'app1/employeedetail.html', {'employee': employee})

def employee_delete(request, employee_id):
    response = requests.delete(f'https://joshya1234.pythonanywhere.com/api/Employee/{employee_id}')
    employee = Employee.objects.filter(id=employee_id).delete()
    id = {"employee_id": employee_id}
    return render(request, 'app1/delete.html', id)


def employee_add(request):
    url = 'https://joshya1234.pythonanywhere.com/api/Employee/?format=json'
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            data = {
            'name': form.cleaned_data['name'],
            'salary': form.cleaned_data['salary'],
            'age': form.cleaned_data['age'],
            'image': form.cleaned_data['image']
            }
            response = requests.post(url, data=data)
            
    else:
        form = EmployeeForm()
    return render(request, 'app1/employee_add.html', {'form': form})

def employee_edit(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            url = 'https://joshya1234.pythonanywhere.com/api/Employee/' + str(employee_id) + '/'
            data = form.cleaned_data
            response = requests.patch(url, json=data)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'app1/employee_edit.html', {'form': form})