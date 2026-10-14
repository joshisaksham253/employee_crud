from django.contrib import admin
from django.urls import path
from . views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_employee/',register_employee,name='register_employee'),
    path('',employee_list,name='employee_list'),
    path('update_employee/<int:id>/',update_employee,name='update_employee'),
    path('delete_employee/<int:id>/',delete_employee,name='delete_employee'),
    
]
