from django import forms
from .models import Car_model




class New_Car_Form(forms.ModelForm):
    class Meta():
        model = Car_model
        fields = '__all__'

    def clean_ano(self):
        ano = self.cleaned_data.get('ano')

        if ano < 2000 :
            self.add_error('ano', 'Não é possivel cadatrar veiculos fabricados antes do ano 2000')
        return ano
    
    def clean_valor(self):
        valor = self.cleaned_data.get('valor')

        if valor < 5000 :
            self.add_error('valor', 'Não é possivel adicionar carros com o valor menor que 5000')

        return valor
    


