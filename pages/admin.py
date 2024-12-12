from django.contrib import admin

from .models import Thematiques, SousThematique, Comment, Actualite

# Register your models here.





class ThematiquesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Thematiques._meta.fields]

admin.site.register(Thematiques, ThematiquesAdmin)



class SousThematiqueAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SousThematique._meta.fields]

admin.site.register(SousThematique, SousThematiqueAdmin)




class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]

admin.site.register(Comment, CommentAdmin)


class ActualiteAdmin(admin.ModelAdmin):
    
    list_display = [field.name for field in Actualite._meta.fields]

admin.site.register(Actualite, ActualiteAdmin)



