from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register_user'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('customer_data/<int:pk>', views.customer_data, name='customer_data'),
    path('delete_customer/<int:pk>', views.delete_customer, name='delete_customer'),
    path('update_customer/<int:pk>', views.update_customer, name='update_customer'),
]
