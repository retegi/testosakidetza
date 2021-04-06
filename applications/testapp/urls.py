from django.urls import include, path
from . import views
from .views import testFilterByModalityAndByUserView

app_name = 'test_app'

urlpatterns = [
    path('test/',
        views.TestPageView.as_view(),
        name='test',
    ),
    path('test/<str:questionModality>/',
        views.testFilterByModalityAndByUserView.as_view(),
        name='test',
    ),
    path('test/',
        views.testFilterByModalityAndByUserView,
        name='test-process',
    ),
    
]