from django.db import models

from django.utils.text import slugify 

from django.contrib.auth.models import User

# Create your models here.

class Thematiques(models.Model):
    titre = models.CharField(max_length=200)
    description=models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to="static/images",blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Thematiques, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_ajout']
        

    def __str__(self):
        return self.titre    


class SousThematique(models.Model):
    thematique_parente = models.ForeignKey(Thematiques, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description_sous_thematique = models.TextField(default='Description par défaut',blank=True)
    date_ajout = models.DateTimeField(auto_now=True)
    periodicite = models.IntegerField(default=2024)  # Utilisation d'un champ entier
    csv_file = models.FileField(upload_to='csv_files/',null=True, blank=True) 
    


    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(SousThematique, self).save(*args, **kwargs)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date_ajout']
        



""" class SousThematique(models.Model):
    thematique_parente = models.ForeignKey(Thematiques, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=False, blank=True)
    description_sous_thematique = models.TextField(default='Description par défaut',blank=True)
    date_ajout = models.DateTimeField(auto_now=True)
    periodicite = models.IntegerField(default=2024)  # Utilisation d'un champ entier
    csv_file = models.FileField(upload_to='csv_files/', null=True, blank=True) 

    def save(self, *args, **kwargs):
        # Créer le slug en combinant le titre et la thématique parente
        parent_slug = slugify(self.thematique_parente.titre) if self.thematique_parente else ''
        titre_slug = slugify(self.titre)
        self.slug = f"{parent_slug}-{titre_slug}"
        super(SousThematique, self).save(*args, **kwargs)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date_ajout'] """


class Comment(models.Model):
    sous_thematique = models.ForeignKey(SousThematique, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]        
    




    

    

    
 

