
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Actualite
from .forms import ActualiteForm



def accueil_actualite(request):

    actualites = Actualite.objects.all()

    context = {"actualites":actualites}

    return render(request, 'actualite/accueil_actualite.html',context)



def ajouter_actualite(request):
    if request.method == 'POST':
        form = ActualiteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accueil_actualite')  # Redirection vers la liste des actualités
    else:
        form = ActualiteForm()
    return render(request, 'actualite/ajouter_actualite.html', {'form': form})



def modifier_actualite(request, slug):
    actualite = Actualite.objects.get(slug=slug)
    if request.method == 'POST':
        form = ActualiteForm(request.POST, request.FILES, instance=actualite)
        if form.is_valid():
            form.save()
            return redirect('accueil_actualite')  # Redirection vers la liste des actualités
    else:
        form = ActualiteForm(instance=actualite)
    return render(request, 'actualite/modifier_actualite.html', {'form': form})




def supprimer_actualite(request, slug):
    actualite = get_object_or_404(Actualite, slug=slug)
    if request.method == 'POST':
        actualite.delete()
        return redirect('accueil_actualite')
    return render(request, 'actualite/supprimer_actualite.html', {'actualite': actualite})    