
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import ContactRequest


from django.contrib import messages  # Importer les messages Django
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import ContactRequest

def accueil_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            objet = form.cleaned_data['objet']
            description = form.cleaned_data['description']

            # Enregistrer dans la base de données
            ContactRequest.objects.create(
                nom=nom,
                prenom=prenom,
                email=email,
                objet=objet,
                description=description
            )

            # Construire le message de l'email
            message = (
                f"Vous avez reçu un nouveau message.\n\n"
                f"Nom : {nom}\n"
                f"Prénom : {prenom}\n"
                f"Email : {email}\n"
                f"Objet : {objet}\n"
                f"\n{description}"
            )

            try:
                # Envoi de l'email
                send_mail(
                    subject=f"Contact Opendatastream : {nom} {prenom}",
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=settings.EMAIL_RECIPIENTS,
                    fail_silently=False,
                )
                # Ajouter un message de succès
                messages.success(request, "Votre message a été envoyé avec succès !")
                return HttpResponseRedirect(reverse('accueil_contact'))
            except Exception:
                # Ajouter un message d'erreur en cas de problème
                messages.error(request, "Une erreur est survenue lors de l'envoi du message.")
                return HttpResponseRedirect(reverse('accueil_contact'))
    else:
        form = ContactForm()

    # Rendu de la page avec le formulaire
    return render(request, 'contact/accueil_contact.html', {'form': form})


