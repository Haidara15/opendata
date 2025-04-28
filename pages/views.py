from django.shortcuts import render

from .models import Thematiques, SousThematique, Comment

from django.shortcuts import render, get_object_or_404, redirect  

from unidecode import unidecode


from django.http import JsonResponse, HttpResponse

import csv

from django.db.models import Q

import urllib.parse


from django.contrib.auth.decorators import login_required

from .forms import CommentForm, SousThematiqueForm, ThematiquesForm
import csv

import openpyxl

from django.contrib import messages




############ partie thématique  ##############################

def page_accueil(request):

    thematiques = Thematiques.objects.all()

    context = {'thematiques':thematiques}

    
    return render(request,"pages/accueil.html",context)


####### CRUD thématique ########### 

from django.contrib import messages

""" def add_thematique(request):
    if request.method == 'POST':
        form = ThematiquesForm(request.POST, request.FILES)
        if form.is_valid():
            thematique = form.save()  # Sauvegarde la thématique
            # Utilisation de la balise <strong> pour le nom de la thématique
            messages.success(request, f"Vous avez ajouté <strong>{thematique.titre}</strong> avec succès !")
            return redirect('accueil')  
    else:
        form = ThematiquesForm()
    return render(request, 'pages/add_thematique.html', {'form': form}) """


from django.http import JsonResponse

def add_thematique(request):
    if request.method == 'POST':
        form = ThematiquesForm(request.POST, request.FILES)
        if form.is_valid():
            thematique = form.save()
            messages.success(request, f"Vous avez ajouté <strong>{thematique.titre}</strong> avec succès !")
            
            # Vérifier si la requête est AJAX
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": True})

            return redirect('accueil')  
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": False, "errors": form.errors})

    else:
        form = ThematiquesForm()
    
    return render(request, 'pages/add_thematique.html', {'form': form})





""" def update_thematique(request, slug):
    thematique = get_object_or_404(Thematiques, slug=slug)
    if request.method == 'POST':
        form = ThematiquesForm(request.POST, request.FILES, instance=thematique)
        if form.is_valid():
            form.save()
            return redirect('accueil')  
    else:
        form = ThematiquesForm(instance=thematique)
    return render(request, 'pages/update_thematique.html', {'form': form, 'thematique': thematique}) """


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string  # Assurez-vous que ceci est ajouté
from .models import Thematiques
from .forms import ThematiquesForm



from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Thematiques
from .forms import ThematiquesForm

def update_thematique(request, slug):
    thematique = get_object_or_404(Thematiques, slug=slug)

    if request.method == "POST":
        form = ThematiquesForm(request.POST, request.FILES, instance=thematique)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})  # AJAX attend cette réponse

    else:
        form = ThematiquesForm(instance=thematique)

    # Si c'est une requête AJAX, on envoie uniquement le formulaire
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'pages/form_update.html', {'form': form, 'thematique': thematique})

    return render(request, 'pages/form_update.html', {'form': form, 'thematique': thematique})






""" def delete_thematique(request, slug):
    thematique = get_object_or_404(Thematiques, slug=slug)
    if request.method == 'POST':
        thematique.delete()
        return redirect('accueil')  
    return render(request, 'pages/delete_thematique.html', {'thematique': thematique}) """

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from pages.models import Thematiques  # Assure-toi que le modèle est bien importé


@csrf_exempt  # Temporairement, si le CSRF pose problème en AJAX
def delete_thematique(request, slug):
    thematique = get_object_or_404(Thematiques, slug=slug)
    if request.method == 'POST':
        try:
            thematique.delete()
            messages.success(request, f"Vous avez supprimé <strong>{thematique.titre}</strong> avec succès !")
            return JsonResponse({'success': True})  # On renvoie un JSON
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Requête invalide'}, status=400)




def recherche(request):
    query = request.GET.get("recherche")
    # Normalisez et convertissez en minuscules
    query_normalized = unidecode(query).lower()
    # Effectuez la recherche en utilisant les titres normalisés
    thematiques_filtred = Thematiques.objects.all()
    thematiques_filtred = [thematique for thematique in thematiques_filtred if query_normalized in unidecode(thematique.titre).lower()]
    return render(request, 'pages/recherche.html', context={"query_normalized":query_normalized,"thematiques_filtred": thematiques_filtred})












############ Partie sous-thématiques #################################

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Thematiques, SousThematique




def thematique_detail(request, slug):
    thematique = get_object_or_404(Thematiques, slug=slug)
    sous_thematiques = SousThematique.objects.filter(thematique_parente=thematique)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Traitement pour les requêtes AJAX
        selected_thematiques = request.GET.getlist('selected_thematiques')
        selected_periodicities = request.GET.getlist('selected_periodicities')

        if selected_thematiques:
            sous_thematiques = sous_thematiques.filter(titre__in=selected_thematiques)
        if selected_periodicities:
            sous_thematiques = sous_thematiques.filter(periodicite__in=selected_periodicities)

        data = {
            'sous_thematiques': list(sous_thematiques.values('titre', 'description_sous_thematique', 'periodicite', 'slug')),
        }
        return JsonResponse(data)

    titres_uniques = sous_thematiques.values_list('titre', flat=True).distinct()

    periodicites_uniques = set(sous_thematiques.values_list('periodicite', flat=True).distinct())

    

    context = {
        'thematiques': thematique,
        'sous_thematiques': sous_thematiques,
        'titres_uniques': titres_uniques,
        'periodicites_uniques': periodicites_uniques
    }

    return render(request, 'pages/thematique_detail.html', context)











from django.http import JsonResponse
import urllib.parse
from unidecode import unidecode
from django.db.models import Q


def filter_sous_thematiques(request):

    thematiques_selectionnees = request.GET.getlist('selected_thematiques')

    periodicites_selectionnees = request.GET.getlist('selected_periodicities')

    terme_recherche = request.GET.get('search')

    sous_thematiques = SousThematique.objects.all()

    if thematiques_selectionnees:
        thematiques_selectionnees_decodees = [urllib.parse.unquote_plus(thematique) for thematique in thematiques_selectionnees]
        sous_thematiques = sous_thematiques.filter(thematique_parente__titre__in=thematiques_selectionnees_decodees)

    if periodicites_selectionnees:
        periodicites_selectionnees_decodees = [urllib.parse.unquote_plus(periodicite) for periodicite in periodicites_selectionnees]
        sous_thematiques = sous_thematiques.filter(periodicite__in=periodicites_selectionnees_decodees)

    if terme_recherche:
        terme_recherche = urllib.parse.unquote(terme_recherche)
        normalized_search_term = unidecode(terme_recherche).lower()

        print("Le mot recherché :", terme_recherche)
        print("Le mot normalisé :", normalized_search_term)

        sous_thematiques = [
            item for item in sous_thematiques
            if (
                isinstance(item.titre, str) and normalized_search_term in unidecode(item.titre).lower()
            ) or (
                isinstance(item.description_sous_thematique, str) and normalized_search_term in unidecode(item.description_sous_thematique).lower()
            ) or (
                isinstance(item.periodicite, int) and normalized_search_term in str(item.periodicite)
            )
        ]

    sous_thematiques_filtrees = [
        {
            'titre': sous_thematique.titre,
            'description_sous_thematique': sous_thematique.description_sous_thematique,
            'periodicite': sous_thematique.periodicite,
            'thematique_parente': sous_thematique.thematique_parente.titre,
            'url_slug': sous_thematique.slug
        }
        for sous_thematique in sous_thematiques
    ]

    return JsonResponse({'sous_thematiques': sous_thematiques_filtrees})





############ Page toutes les tables ######################################

def tables(request):

    valeurs_uniques_themes = Thematiques.objects.values_list('titre', flat=True).distinct()

    valeurs_uniques_periodicite = SousThematique.objects.values_list('periodicite', flat=True).distinct().order_by('-periodicite')

    context = {

        "valeurs_uniques_themes": valeurs_uniques_themes,

        "valeurs_uniques_periodicite": valeurs_uniques_periodicite
    }

    return render(request, 'pages/tables.html', context)






################## Page détail de sous-thématique ################

def sous_thematique_detail(request,slug):

    sous_thematique = get_object_or_404(SousThematique, slug=slug)

    # Vérifier si la sous-thématique a un fichier CSV associé
    csv_data = None
    if sous_thematique.csv_file:
        csv_data = []
        with open(sous_thematique.csv_file.path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # Lire la première ligne comme en-têtes
            for row in csv_reader:
                row_data = dict(zip(headers, row))  # Convertir chaque ligne en un dictionnaire
                csv_data.append(row_data)

    # Gérer les commentaires
    comments = sous_thematique.comments.filter(parent__isnull=True)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('connexion')
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            content = form.cleaned_data['content']
            parent_id = form.cleaned_data.get('parent_id')
            parent_comment = Comment.objects.get(id=parent_id) if parent_id else None
            Comment.objects.create(sous_thematique=sous_thematique, user=user, content=content, parent=parent_comment)
            return redirect('sous_thematique_detail', slug=sous_thematique.slug)
    else:
        form = CommentForm()

    context = {
        'sous_thematique': sous_thematique,
        'csv_data': csv_data,
        'comments': comments,
        'form': form,
    }

    return render(request, 'pages/sous_thematique_detail.html', context)




###### Partie des vues : Sous-thématiques ########

def add_sous_thematique(request):
    if request.method == 'POST':
        form = SousThematiqueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tables')  # Remplacez par votre URL de succès
    else:
        form = SousThematiqueForm()
    return render(request, 'pages/add_sous_thematique.html', {'form': form})



def update_sous_thematique(request, slug):
    sous_thematique = get_object_or_404(SousThematique, slug=slug)
    if request.method == 'POST':
        form = SousThematiqueForm(request.POST, request.FILES, instance=sous_thematique)
        if form.is_valid():
            form.save()
            return redirect('tables')  # Remplacez par votre URL de succès
    else:
        form = SousThematiqueForm(instance=sous_thematique)
    return render(request, 'pages/update_sous_thematique.html', {'form': form,'sous_thematique':sous_thematique})



def delete_sous_thematique(request, slug):
    sous_thematique = get_object_or_404(SousThematique, slug=slug)
    if request.method == 'POST':
        sous_thematique.delete()
        return redirect('accueil')  # Remplacez par votre URL de succès
    return render(request, 'pages/delete_sous_thematique.html', {'sous_thematique': sous_thematique})






########## Boutons de téléchargement #######################################

def download_csv(request, sous_thematique_id):
    sous_thematique = get_object_or_404(SousThematique, id=sous_thematique_id)

    if sous_thematique.csv_file:
        # Ouvrir le fichier CSV
        csv_file = sous_thematique.csv_file.path
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Lire l'en-tête

            # Trier par ordre alphabétique sur la première colonne (header[0])
            sorted_rows = sorted(reader, key=lambda row: row[0])

            # Créer la réponse HTTP pour le téléchargement
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{sous_thematique.titre}_sorted.csv"'

            writer = csv.writer(response)
            writer.writerow(header)  # Écrire l'en-tête
            writer.writerows(sorted_rows)  # Écrire les lignes triées

            return response
    else:
        # Si aucun fichier n'est associé, retourner une réponse vide ou une erreur appropriée
        return HttpResponse("Fichier CSV non trouvé pour cette sous-thématique.", status=404)
    



def download_xlsx(request, sous_thematique_id):
    sous_thematique = get_object_or_404(SousThematique, id=sous_thematique_id)

    if sous_thematique.csv_file:
        # Ouvrir le fichier CSV
        csv_file = sous_thematique.csv_file.path
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Lire l'en-tête
            worksheet.append(header)  # Ajouter l'en-tête à la feuille Excel

            # Trier par ordre alphabétique sur la première colonne (header[0])
            sorted_rows = sorted(reader, key=lambda row: row[0])

            # Ajouter les lignes triées à la feuille Excel
            for row in sorted_rows:
                worksheet.append(row)

        # Créer la réponse HTTP pour le téléchargement
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{sous_thematique.titre}_sorted.xlsx"'
        workbook.save(response)

        return response
    else:
        # Si aucun fichier n'est associé, retourner une réponse vide ou une erreur appropriée
        return HttpResponse("Fichier CSV non trouvé pour cette sous-thématique.", status=404)
    


def download_json(request, sous_thematique_id):
    sous_thematique = get_object_or_404(SousThematique, id=sous_thematique_id)

    if sous_thematique.csv_file:
        # Ouvrir le fichier CSV
        csv_file = sous_thematique.csv_file.path
        data = []

        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)

        # Créer la réponse JSON pour le téléchargement
        response_data = {'data': data}
        return JsonResponse(response_data, json_dumps_params={'indent': 2})
    else:
        # Si aucun fichier n'est associé, retourner une réponse vide ou une erreur appropriée
        return HttpResponse("Fichier CSV non trouvé pour cette sous-thématique.", status=404)
    

































    






























