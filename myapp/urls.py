from django.urls import path,re_path
from myapp import views

urlpatterns = [
    path ('',views.home, name='home'),
]