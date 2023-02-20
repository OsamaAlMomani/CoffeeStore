from django.urls import path,re_path
from . import views

urlpatterns = [
    path('dishes/<str:dish>',views.menuitems),
]