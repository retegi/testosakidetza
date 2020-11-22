from django.contrib import admin
from .models import Modality
from .models import Test

# Register your models here.

class ModalityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(Modality,ModalityAdmin)

class TestAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'question',
        'a',
        'b',
        'c',
        'd',
        'answer',
        'nameModality'
    )
admin.site.register(Test,TestAdmin)