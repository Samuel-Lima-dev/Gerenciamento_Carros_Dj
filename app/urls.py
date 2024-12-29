"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from car.views import home_view, new_car_view
from accounts.views import login_view, new_user_view, logout_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name=''),
    path('new_car/', new_car_view, name='cadastro_carros'),
    path('login/', login_view, name='login'),
    path('new_user/', new_user_view, name='cadastro_usuario'),
    path('logout/', logout_view, name='sair')

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
