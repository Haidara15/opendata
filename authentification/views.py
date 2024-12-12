from django.shortcuts import redirect, render

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

from .form import UserForm

from django.contrib import messages



def page_inscription(request):
    form = UserForm
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Votre compte a été créé")
            return redirect('connexion')
        else:
            messages.error(request,form.errors)
    return render(request,'authentification/inscription.html', context={'form':form})



def page_connexion(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Vous êtes connecté')
            return redirect("accueil") 
        else:
            messages.error(request,"Erreur d'authentification")    
    return render(request,'authentification/connexion.html', context={})


@login_required
def deconnection(request):
    logout(request)
    messages.success(request, 'Vous vous êtes déconnecté')
    return redirect('connexion')
