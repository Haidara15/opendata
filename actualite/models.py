from django.db import models

from django.utils.text import slugify


class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    description=models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to="static/images",blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Actualite, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.titre
