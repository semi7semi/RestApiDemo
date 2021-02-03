from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.base import View
from rest_api.forms import MyUserCreation

from .models import CarType, Car

class CreateCarView(CreateView):
    model = Car
    success_url = '/create_car/'
    fields = '__all__'
    template_name = 'form.html'


class CreateCarTypeView(CreateView):
    model = CarType
    success_url = '/create_car_type/'
    fields = '__all__'
    template_name = 'form.html'

class ShowAllView(View):

    def get(self, request):
        cars = Car.objects.all()
        types = CarType.objects.all()
        costam = render(request, 'rest_api/show_all.html', {'cars':cars, 'types':types})
        return costam

def get_cars_by_type(request):
    type_ids = request.GET.getlist('type_ids')
    if type_ids is not None:
        cars = Car.objects.filter(car_type__in=type_ids).distinct()
    else:
        cars = Car.objects.all()
    return render(request, "api_cars.html", {'cars':cars, 'form':MyUserCreation()})
    # return HttpResponse(str(request.GET.getlist("kategorie")))


