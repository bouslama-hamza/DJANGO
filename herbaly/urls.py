from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'herbaly-home'),
    path('sign_up/', views.sign_up , name = 'herbaly-sign-up'),
    path('app/', views.app , name = 'herbaly-app'),
    path('active_account/', views.active_account , name = 'herbaly-active-account'),
    path('google_cloud/', views.google_cloud , name = 'herbaly-google-cloud'),
    path('manage_account/', views.manage_account , name = 'herbaly-manage-account'),
    path('forget_password/', views.forget_password , name = 'herbaly-forget-password'),
    path('change_password/', views.change_password , name = 'herbaly-change_password'),
    path('data_base/', views.data_base , name = 'herbaly-data-base'),  
]