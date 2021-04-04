from django.urls import include, path
from . import views
from .views import testFilterByModalityAndByUser

app_name = 'test_app'

urlpatterns = [
    path('test/',
        views.TestPageView.as_view(),
        name='test',
    ),
    path('test/<str:questionModality>/',
        views.testFilterByModalityAndByUser,
        name='test',
    ),
]