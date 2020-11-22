from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView
)
from .models import Test
from .models import Modality


class TestPageView(TemplateView):
    template_name = "test/question.html"