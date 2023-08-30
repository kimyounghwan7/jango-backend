from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('list/', views.show_users, name='user_list'),
    path('<int:user_id>/', views.show_user, name='user_one'),
    path('register/', views.register_user, name='user_register'),
    path('modify/', views.modify_user, name='user_modify'),
    path('upload/', views.register_user_image, name='user_image_reg'),
    path('image/', views.show_user_image, name='user_image_show'),
]
########