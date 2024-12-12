
from django.urls import path

from pages import views 

urlpatterns = [
    path('', views.page_accueil, name="accueil"),

    path('add_thematique/', views.add_thematique, name='add_thematique'),
    path('update/<slug:slug>/', views.update_thematique, name='update_thematique'),
    path('delete/<slug:slug>/', views.delete_thematique, name='delete_thematique'),


    path('add_sous_thematique/', views.add_sous_thematique, name='add_sous_thematique'),
    path('update_sous_thematique/<slug:slug>/', views.update_sous_thematique, name='update_sous_thematique'),
    path('delete_sous_thematique/<slug:slug>/', views.delete_sous_thematique, name='delete_sous_thematique'),

    path('thematiques/<slug:slug>/', views.thematique_detail, name='page_detail'),

    path('sous-thematiques/<slug:slug>/', views.sous_thematique_detail, name='sous_thematique_detail'),
    path('recherche/', views.recherche, name='recherche'),
    path('tables/', views.tables, name='tables'),
    path('filter_sous_thematiques/', views.filter_sous_thematiques, name='filter_sous_thematiques'),


    
    path('sous-thematique/<int:sous_thematique_id>/download-csv/', views.download_csv, name='download_csv'),
    path('sous-thematique/<int:sous_thematique_id>/download-xlsx/', views.download_xlsx, name='download_xlsx'),
    path('sous-thematique/<int:sous_thematique_id>/download-json/', views.download_json, name='download_json'),

    #### Actualité #### 

    path('actualite/', views.actualite, name='actualite'),
    path('actualite/ajouter/', views.ajouter_actualite, name='ajouter_actualite'),
    path('actualite/modifier/<slug:slug>/', views.modifier_actualite, name='modifier_actualite'),
    path('actualite/supprimer/<slug:slug>/', views.supprimer_actualite, name='supprimer_actualite'),
]


