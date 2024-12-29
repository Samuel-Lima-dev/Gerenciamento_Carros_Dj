from django.db import models


class Brand_model(models.Model):
    marca = models.CharField(max_length=50)

    def __str__(self):
        return self.marca


class Car_model(models.Model):
    modelo = models.CharField(max_length = 100, blank = False, null = False)
    marca = models.ForeignKey(Brand_model, on_delete=models.CASCADE)
    ano = models.IntegerField(blank = True, null = True)
    valor = models.DecimalField(max_digits=10, decimal_places=2 , blank=True)
    imagem = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.modelo
