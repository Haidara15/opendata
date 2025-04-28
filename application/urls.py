

from django.urls import path

from .views import accueil, download_csv, download_json, download_xlsx


urlpatterns = [
    path('', accueil, name="accueil"),
    path('download-csv/', download_csv, name='download_csv'),
    path('download-xlsx/', download_xlsx, name='download_xlsx'), 
    path('download-json/', download_json, name='download_json'),
]