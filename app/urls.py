from django.contrib import admin
from django.urls import path
from car.views import HomePageView, CreateNewCarView, DetailCarView, CarUpdateView, CarDeleteView

from accounts.views import login_view, new_user_view, logout_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomePageView.as_view(), name='home'),
    path('new_car/', CreateNewCarView.as_view(), name='cadastro_carros'),

    path('login/', login_view, name='login'),
    path('new_user/', new_user_view, name='cadastro_usuario'),
    path('logout/', logout_view, name='sair'),

    path('car/<int:pk>',DetailCarView.as_view(), name='detalhes' ),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='delete'),


]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


