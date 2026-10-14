from django.shortcuts import render,redirect,get_object_or_404
from . models import Employee
# Create your views here.
def register_employee(request):
    
    if request.method=="POST":
        
        Employee.objects.create(
        name=request.POST.get('name'),
        age=request.POST.get('age'),
        email=request.POST.get('email'),
        phone=request.POST.get('phone'),
        address=request.POST.get('address'),
        department=request.POST.get('department'),
        salary=request.POST.get('salary'),
        joining_date=request.POST.get('joining_date'),
        
        
        )
        return redirect('employee_list')
    return render(request,'register_employee.html')
        

def employee_list(request):
    data=Employee.objects.all()
    return render(request,'employee_list.html',{'data':data})

def update_employee(request,id):
    
    employee=get_object_or_404(Employee,id=id)
    
    if request.method=='POST':
        employee.name=request.POST.get('name')
        employee.age=request.POST.get('age')
        employee.email=request.POST.get('email')
        employee.phone=request.POST.get('phone')
        employee.address=request.POST.get('address')
        employee.department=request.POST.get('department')
        employee.salary=request.POST.get('salary')
        employee.joining_date=request.POST.get('joining_date')
        
        employee.save()
        
        return redirect('employee_list')
    
    return render(request,'update_employee.html',{'employee':employee})

def delete_employee(request,id):
    
    employee=get_object_or_404(Employee,id=id)
    
    if request.method=='POST':
        employee.delete()
        
        return redirect('employee_list')
    
    return render(request,'delete_employee.html',{'employee':employee})  
  
    
            
    
    
    

    
    
