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
from django.db.models import Q


class TestPageView(TemplateView):
    template_name = "test/question.html"


"""def testFilterByModalityAndByUser(request, questionModality):
    model = Test
    msg='Estás en la modalidad ' + questionModality
    test = Test.objects.all().filter(nameModality__name=questionModality).order_by('number')[:10]
    print(test[0].question)
    if request.user.is_authenticated:
        username = request.user.username
        print(username)
    msg='Estás en la modalidad ' + questionModality + ' usuario ' + username
    messages.success(request, msg, test)
    return redirect(reverse_lazy('test_app:test'),args=(test))"""


class testFilterByModalityAndByUserView(ListView):
    model = Test
    template_name = 'test/question.html'

    def get_queryset(self):
        questionMod = self.kwargs['questionModality']
        print(questionMod)

        
        #name = self.request.GET.get('kword', '')
        if questionMod:
            object_list = Test.objects.all().filter(nameModality__name=questionMod).order_by('number')[:1]
        else:
            object_list = Test.objects.all()
        return object_list
    login_url = reverse_lazy('test_app:test')

    #Aquí se tiene que retornar desde el formulario: Letra seleccionada, Modalidad de preguntas, Nºpregunta y Usuario.
    def post(self, request):
        if request.method == 'POST':
            print("Es post")
            print("Es post")
            print("Es post")
            print("Es post")
            """if request.user.is_authenticated:
                username = request.user.username
                print(username)"""
            # create a form instance and populate it with data from the request:
            #form = NameForm(request.POST)

            """user= request.POST.get('userId')
            testModality = request.POST.get('testModality')
            numberTest = request.POST.get('numberTest')
            answerLetter = request.POST.get('answerLetter')
            answerOk= request.POST.get('answerOk')"""
            
        
            # check whether it's valid:
            if form.is_valid():
                pass
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/thanks/')








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