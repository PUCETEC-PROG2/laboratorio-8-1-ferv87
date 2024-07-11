from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name=models.CharField(max_length=30,null=False)
    POKEMON_TYPES = {
        ('A', 'Agua'),
        ('E', 'Electrico'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('L', 'Lagartija'),
    }
    type=models.CharField(max_length=30, choices=POKEMON_TYPES, null=False)
    weight=models.DecimalField(null=False,default=1, max_digits=4, decimal_places=2)
    height=models.DecimalField(null=False,default=1, max_digits=4, decimal_places=2)
    
    def __str__(self) -> str:
        return self.name