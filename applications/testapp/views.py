from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView,
    ListView
)
from .models import Test
from .models import Modality
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib import messages


class TestPageView(TemplateView):
    template_name = "test/question.html"


def testFilterByModalityAndByUser(request, questionModality):
    model = Test
    msg='Estás en la modalidad ' + questionModality

    test = Test.objects.all().filter(nameModality__name=questionModality).order_by('number')[:10]
    print(test)

    if request.user.is_authenticated:
        username = request.user.username
        print(username)
    
    msg='Estás en la modalidad ' + questionModality + ' usuario ' + username

    messages.success(request, msg)
    return redirect(reverse_lazy('test_app:test'))


"""def testFilterByModalityAndByUser(request, questionModality):
    model = Test
    msg='Estás en la modalidad ' + questionModality

    test = Test.objects.all().filter(nameModality__name=questionModality)
    print(test)

    if request.user.is_authenticated:
        username = request.user.username
        print(username)
    
    messages.success(request, msg)
    return redirect(reverse_lazy('test_app:test'))"""



"""class InstallationGalleryListView(ListView):
    model = ImageInstallation
    template_name = 'installation/gallery_installation.html'
    def get_queryset(self):
        name = self.kwargs['pk']
        if name:
            object_list = self.model.objects.all().filter(installation__id = name)
        #else:
        #    object_list = self.model.objects.all().order_by('id')
        return object_list"""