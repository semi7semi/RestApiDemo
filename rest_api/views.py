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
    type_id = request.GET.get('type_id')
    if type_id is not None:
        car_type = CarType.objects.get(pk=type_id)
        cars = Car.objects.filter(car_type=car_type)
    else:
        cars = Car.objects.all()
    return render(request, "api_cars.html", {'cars':cars, 'form':MyUserCreation()})
    # return HttpResponse(str(request.GET.getlist("kategorie")))


