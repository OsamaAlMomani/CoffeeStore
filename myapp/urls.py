from django.urls import path,re_path
from myapp import views

urlpatterns = [
    path ('home/', views.CAF),
]