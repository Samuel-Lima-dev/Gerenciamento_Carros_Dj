from django.shortcuts import render, redirect
from .models import Car_model
from .forms import New_Car_Form

from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



    
class HomePageView(ListView):
    model = Car_model
    template_name = 'homepage.html'
    context_object_name = 'carros'

    def get_queryset(self):
        #pegar todos o carros cadastrados
        carros = super().get_queryset().order_by('modelo')
        #pegar o valor de busca do usuario
        busca = self.request.GET.get('busca')

        if busca:
            carros = carros.filter(modelo__icontains = busca)
        return carros


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
            return redirect('home')
        return render(
            request,
            'new_car.html',
            {'form': new_car }
        )



class DetailCarView(DetailView):
    model = Car_model
    template_name = 'detail_car.html'

    
@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateNewCarView(CreateView):
    model = Car_model
    form_class = New_Car_Form
    template_name = 'new_car.html'
    success_url = '/new_car/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car_model
    form_class = New_Car_Form
    template_name = 'update.html'

    def get_success_url(self):
        return reverse_lazy('detalhes', kwargs = {'pk': self.object.pk})  


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car_model
    template_name = 'car_delete.html'
    success_url = '/home/'
