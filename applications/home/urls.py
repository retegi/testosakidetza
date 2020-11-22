from django.urls import include, path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('',
        views.LoginView.as_view(),
        name='login',
    ),
    path('user_registration/',
        views.UserRegistrationView.as_view(),
        name='user_registration',
    ),
    path('home/',
        views.HomePageView.as_view(),
        name='home',
    ),
    path('aviso_lecal/',
        views.AvisoLegalView.as_view(),
        name='aviso_legal',
    ),
    path('politica_de_privacidad/',
        views.PoliticaDePrivacidadView.as_view(),
        name='politica_de_privacidad',
    ),
    path('politica_de_cookies/',
        views.PoliticaDeCookiesView.as_view(),
        name='politica_de_cookies',
    ),
    

]