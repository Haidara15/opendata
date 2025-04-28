from django.db import models


class ContactRequest(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=True)  
    prenom = models.CharField(max_length=100, null=True, blank=True)  
    email = models.EmailField()
    objet = models.CharField(max_length=200, null=True, blank=True)  
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



