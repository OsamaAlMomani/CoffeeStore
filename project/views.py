from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
def error404(req ,exp):
    return HttpResponseNotFound("<h1>404 : Page Not Found!!</h1>")