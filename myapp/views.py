from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def menuitems(request,dish):
    item = {
        'pasta':'Italian food',
        'konafa':'Jordanian desert',
        'cheese': 'cheese is delicious'
    }
    discreiption = item [dish]
    return HttpResponse(f"<h2> {dish} discription : {discreiption}")