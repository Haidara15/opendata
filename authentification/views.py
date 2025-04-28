from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sessions.models import Session
from django.utils.timezone import now
from .form import UserForm
from .models import EmailVerificationToken
import uuid
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import EmailVerificationToken
from .form import UserForm
import uuid

def page_inscription(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Désactiver l'utilisateur
            user.save()
            token = str(uuid.uuid4())
            EmailVerificationToken.objects.create(user=user, token=token)
            send_verification_email(user, request)
            messages.success(request, "Un email de confirmation a été envoyé. Veuillez vérifier votre boîte de réception.")
            return redirect('connexion')
        else:
            messages.error(request, "Erreur lors de l'inscription. Veuillez corriger les champs.")
    return render(request, 'authentification/inscription.html', {'form': form})



def page_connexion(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if not user.is_active:
                messages.error(request, "Veuillez vérifier votre adresse email avant de vous connecter.")
                return redirect('connexion')
        except User.DoesNotExist:
            pass

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Ajouter le message avant la redirection
            messages.success(request, "Vous vous êtes connecté.")
            return redirect('accueil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'authentification/connexion.html')








def send_verification_email(user, request):
    token = EmailVerificationToken.objects.get(user=user).token
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    domain = request.get_host()
    protocol = 'https' if request.is_secure() else 'http'
    context = {
        'user': user,
        'token': token,
        'uidb64': uidb64,
        'domain': domain,
        'protocol': protocol,
    }
    subject = 'Confirmez votre adresse email'
    message = render_to_string('authentification/email_verification.html', context)
    email = EmailMessage(subject, message, to=[user.email])
    email.content_subtype = "html"
    email.send()






def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        verification_token = EmailVerificationToken.objects.get(user=user, token=token)

        if verification_token.is_expired():
            verification_token.delete()
            messages.error(request, "Le lien de vérification a expiré.")
            return redirect('connexion')

        # Activer l'utilisateur
        user.is_active = True
        user.save()
        verification_token.delete()

        messages.success(request, "Votre adresse email a été vérifiée. Vous pouvez maintenant vous connecter.")
    except (User.DoesNotExist, EmailVerificationToken.DoesNotExist):
        messages.error(request, "Le lien de vérification est invalide ou a expiré.")
    return redirect('connexion')






# Déconnexion
@login_required
def deconnection(request):
    logout(request)
    messages.success(request, "Vous vous êtes déconnecté.")
    return redirect('connexion')
