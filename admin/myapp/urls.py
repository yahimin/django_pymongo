from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('get_list/',views.get_list,name='get_list'),
    path('get_name_list',views.get_name_list,name='get_name_list'),
]
