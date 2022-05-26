from django.db import models

# Create your models here.
class Drug(models.Model):
    name = models.CharField(
        'Nome', max_length=30
        )
    
    slug = models.SlugField(
        'Identificação única'
        )
    
    chemical_name = models.CharField(
        'Nome químico', blank=True
        )
    
    description = models.TextField(
        'Sobre a droga', blank=True, 
    )
    
    image = models.ImageField(
        upload_to='core/images', verbose_name='Imagem',
        null=True, blank=True
    )
    
    
    STATUS_CHOICES = (
        (0, 'Legal'),
        (1, 'Ilegal'),
    )
    legality = models.IntegerField(
        'Legalidade', choices=STATUS_CHOICES, default=0, blank=True
        )
    
    STATUS_CHOICES = (
        (0, 'Baixa'),
        (1, 'Mediana'),
        (2, 'Alta'),
    )
    dangerousness = models.IntegerField(
        'Periculosidade', choices=STATUS_CHOICES, default=0, blank=True
        )