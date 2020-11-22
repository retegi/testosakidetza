from django.urls import include, path
from . import views

app_name = 'test_app'

urlpatterns = [
    path('test/',
        views.TestPageView.as_view(),
        name='test',
    ),
]