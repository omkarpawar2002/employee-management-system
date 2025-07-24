from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required

@login_required(login_url='sign_in')
def create_emp(request):
    form = EmployeeForm()
    if(request.method == 'POST'):
        form = EmployeeForm(request.POST)
        if(form.is_valid()):
            form.save() 
            return redirect('show_emp')
        
    template_name = 'emp_info/create_emp.html'
    context = {'form':form}
    return render(request,template_name,context)

@login_required(login_url='sign_in')
def show_emp(request):
    objs = Employee.objects.all()
    template_name = 'emp_info/show_emp.html'
    context = {'records':objs}
    return render(request,template_name,context)

def update_emp(request,pk):
    objs = Employee.objects.get(eid=pk)
    form = EmployeeForm(instance=objs)
    if(request.method == 'POST'):
        form = EmployeeForm(request.POST,instance=objs)
        if(form.is_valid()):
            form.save()
            return redirect('show_emp')
        
    template_name = 'emp_info/update_emp.html'
    context = {'form':form}
    return render(request,template_name,context)

def delete_emp(request,pk):
    obj = Employee.objects.get(eid=pk)
    form = EmployeeForm(instance = obj)
    if(request.method == 'POST'):
        form = EmployeeForm(request.POST,instance=obj)
        obj.delete()
        return redirect('show_emp')
    
    template_name = 'emp_info/delete_emp.html'
    context = {'form':obj}
    return render(request,template_name,context)
