from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/',views.dashboard,name='profile'),
    path('id/<str:id>',views.request_with_param,name='param-req'),
]
