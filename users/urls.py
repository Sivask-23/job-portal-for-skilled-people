from django.urls import path
from . import views


urlpatterns = [
    #path('register-applicant', views.register_applicants,name='register-applicants'),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('ok', views.ok,name='ok'),
    
]