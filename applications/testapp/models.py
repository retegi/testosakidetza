from django.db import models
from datetime import datetime

# Create your models here.

class Modality(models.Model):
    name=models.CharField('Modalidad',max_length=100, null=True,blank=True)

    class Meta:
        verbose_name = 'Modalidad'
        verbose_name_plural = 'Modalidades'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Test(models.Model):
    ANSWER=(('1','A'),('2','B'),('3','C'),('4','D'))
    number=models.IntegerField('Nº',null=True,blank=True)
    question=models.TextField('Pregunta',null=True,blank=True)
    a=models.TextField('A',null=True,blank=True)
    b=models.TextField('B',null=True,blank=True)
    c=models.TextField('C',null=True,blank=True)
    d=models.TextField('D',null=True,blank=True)
    answer=models.CharField('Respuesta',max_length=1,choices=ANSWER, null=True, blank=True)
    nameModality=models.ForeignKey(Modality,on_delete=models.CASCADE,null=True,blank=True)
    observations=models.TextField('Observaciones',null=True,blank=True)


    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Test'
        ordering = ['number']

    def __str__(self):
        return str(self.number)


"""class RespuestasUsuarios(models.Model):
    ABCD_CHOICES = (
    ('-','-'),
    ('a', 'A'),
    ('b','B'),
    ('c','C'),
    ('d','D'),
)
    usuario=model.ForeignKey(User)
    test=models.ForeignKey(Test)
    answerABCG=models.CharField(max_length=2, choices=ABCD_CHOICES, default='-')
    datetime=models.DateTimeField(auto_now_add=True, blank=True)
    correctoAnswer=models.BooleanField('Correcto')"""

