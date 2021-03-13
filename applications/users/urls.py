from django.urls import include, path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('',
        views.UserLoginView.as_view(),
        name='user-login',
    ),
    path('user_registration/',
        views.UserRegistrationView.as_view(),
        name='user-registration',
    ),
    path('user_logout/',
        views.UserLogoutView.as_view(),
        name='user-logout',
    ),
]