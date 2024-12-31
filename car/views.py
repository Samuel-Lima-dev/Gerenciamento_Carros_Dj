from django.shortcuts import render, redirect
from .models import Car_model
from .forms import New_Car_Form
from django.views import View
from django.views.generic import ListView



class HomeView(View):

    def get(self, request):
        carros = Car_model.objects.all().order_by('modelo')
        busca = request.GET.get('busca')

        if busca:
            carros = Car_model.objects.filter(modelo__icontains = busca)

        return render(
            request,
            'homepage.html',
            {'carros': carros}
        )
    

class NewCarView(View):

    def get(self, request):
        new_car = New_Car_Form()
        return render(
            request,
            'new_car.html',
            {'form': new_car}
        )

    def post(self, request):
        new_car = New_Car_Form(request.POST, request.FILES)
        if new_car.is_valid():
            new_car.save()
            return redirect('')
        return render(
            request,
            'new_car.html',
            {'form': new_car }
        )

