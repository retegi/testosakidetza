from django.db import models

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


    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Test'
        ordering = ['number']

    def __str__(self):
        return self.number


