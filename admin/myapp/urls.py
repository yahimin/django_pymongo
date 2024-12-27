from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('get_list/',views.get_list,name='get_list'),
    path('get_name_list',views.get_name_list,name='get_name_list'),
    path('add_user/',views.add_user,name='add_user'),
    path('add_detail_user/',views.add_detail_user , name ='add_detail_user'),
    path('cate/',views.get_cate_name_list,name='get_cate_name_list')
]
