from django.db import models

class MathWord(models.Model):
    fields = [
        ('General','General'),
        ('Geometry','Geometry'),
        ('Algebra and Calculus','Algebra and Calculus'),
    ]

    english = models.CharField(max_length=100)
    french = models.CharField(max_length=100)
    arabic = models.CharField(max_length=100)
    field = models.CharField(max_length=100,null=True,blank=True,choices=fields)

    def __str__(self):
        return self.english

class PCWord(models.Model):
    fields = [
        ('General','General'),
        ('Electricity','Electricity'),
        ('Optics','Optics'),
        ('Waves','Waves'),
        ('Nuclear transformation','Nuclear transformation'),
        ('Matter','Matter'),
        ('Measurements in chemistry','Measurements in chemistry'),
        ('Mechanics','Mechanics'),
        ('Chemical reactions','Chemical reactions'),
        ('Organic chemistry','Organic chemistry'),

    ]
    english = models.CharField(max_length=100)
    french = models.CharField(max_length=100)
    arabic = models.CharField(max_length=100)
    field = models.CharField(max_length=100,null=True,blank=True,choices=fields)

    def __str__(self):
        return self.english

class SVTWord(models.Model):
    fields = [
        ('General','General'),
        ('Ecology','Ecology'),
        ('Reproduction in plants','Reproduction in plants'),
        ('Geology','Geology'),
        ('Genetics','Genetics'),
        ('Organic matter','Organic matter'),
        ('Nerves: Neurons and hormones','Nerves: Neurons and hormones'),
        ('Reproduction in humans ','Reproduction in humans '),
        ('Immunology','Immunology'),
    ]
    
    english = models.CharField(max_length=100)
    french = models.CharField(max_length=100)
    arabic = models.CharField(max_length=100)
    field = models.CharField(max_length=100,null=True,blank=True,choices=fields)


    def __str__(self):
        return self.english