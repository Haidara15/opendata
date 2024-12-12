from django.db import models





# Create your models here.

class Datatable(models.Model):
    periodicite = models.CharField(max_length=100, default="Non renseigné")
    data = models.IntegerField()

    def __str__(self):
        return f'{self.data} - {self.periodicite}'
    
    class Meta:
        ordering = ['-data']





