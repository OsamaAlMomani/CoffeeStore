from django.urls import path,re_path
from myapp import views

urlpatterns = [
    path ('home/',views.home, name='home'),
    path ('CAF/', views.CAF, name='CAF'),
]