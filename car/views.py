from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Car_model
from .forms import New_Car_Form



def home_view(request):

    carros = Car_model.objects.all().order_by('modelo')
    busca = request.GET.get('busca')

    if busca:
        carros = Car_model.objects.filter(modelo__icontains = busca)
    
    return render(
        request,
        'homepage.html',
        {'carros': carros}
    )

def new_car_view (request):
    
    if request.method == 'POST':
        new_car_form = New_Car_Form(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('')
    else:
        new_car_form = New_Car_Form()

    return render(
        request,
        'new_car.html',
        {'form': new_car_form}
    )