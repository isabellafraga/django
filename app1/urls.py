from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [

    path('calc/', views.calc, name="calc"),
    path('help/', views.help, name="help"),
    path('sp/', views.sp, name="sp"),
    path('registros/', views.registros, name="registros"),
    path('form/', views.form_name, name="form"),
    path('modelform/', views.users, name="modelform"),

]
