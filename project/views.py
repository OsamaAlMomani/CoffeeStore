from django.http import HttpResponse, HttpResponseNotFound
def handler404(req ,exp):
    return HttpResponseNotFound("404 : Page Not Found!!")