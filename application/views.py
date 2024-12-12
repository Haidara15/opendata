from django.shortcuts import render
from application.models import Datatable

## Import/Export CSV XLSX
import csv
import openpyxl
from django.http import HttpResponse
from django.utils.encoding import smart_str

## Pour JSON
import json
from django.http import JsonResponse





def accueil(request):

    donnees_tableau = Datatable.objects.all()

    context = {"donnees_tableau":donnees_tableau}

    return render(request,'application/accueil.html',context) 




def download_csv(request):
    # Récupérer toutes les instances du modèle
    instances = Datatable.objects.all()

    # Nom du fichier CSV de sortie
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    # Créer le writer CSV
    writer = csv.writer(response)

    # Écrire l'en-tête avec les noms de colonne
    header = [field.name for field in Datatable._meta.fields]
    writer.writerow(header)

    # Écrire les données
    for instance in instances:
        # Obtenir les valeurs de toutes les colonnes
        row = [getattr(instance, field) for field in header]
        writer.writerow(row)

    return response


def download_xlsx(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="datatable.xlsx"'
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['periodicite', 'data'])

    for item in Datatable.objects.all():
        ws.append([smart_str(item.periodicite), smart_str(item.data)])

    wb.save(response)
    return response 


def download_json(request):
    data = [{'periodicite': item.periodicite, 'data': item.data} for item in Datatable.objects.all()]
    response_data = {'data': data}
    return JsonResponse(response_data, json_dumps_params={'indent': 2})









