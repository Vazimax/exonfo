from django.db import models

class MathWord(models.Model):
    fields = [
        ('geometry','geometry'),
        ('algebra','algebra'),

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
        ('biology','biology'),
        ('geology','geology'),

    ]
    english = models.CharField(max_length=100)
    french = models.CharField(max_length=100)
    arabic = models.CharField(max_length=100)
    field = models.CharField(max_length=100,null=True,blank=True,choices=fields)

    def __str__(self):
        return self.english