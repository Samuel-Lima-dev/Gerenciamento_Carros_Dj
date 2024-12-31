from django.contrib import admin
from django.urls import path
from car.views import HomeView, NewCarView
from accounts.views import login_view, new_user_view, logout_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name=''),
    path('new_car/', NewCarView.as_view(), name='cadastro_carros'),
    path('login/', login_view, name='login'),
    path('new_user/', new_user_view, name='cadastro_usuario'),
    path('logout/', logout_view, name='sair')

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
