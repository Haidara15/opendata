import os
import sys  # Ajout de sys

# 🛠 Définir la racine du projet (répertoire contenant manage.py)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 🛠 Ajouter la racine du projet au sys.path
sys.path.append(BASE_DIR)

# 🛠 Définir la configuration Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opendata.settings")  # Remplace "opendata" par ton projet

# ✅ Initialiser Django
import django
django.setup()

# Importer les modèles après l'initialisation de Django
from django.utils.text import slugify
from collections import defaultdict
from pages.models import SousThematique

def update_titles_and_slugs():
    """Met à jour les titres et slugs pour garantir unicité par thematique_parente."""

    # Regrouper les doublons (même titre et même thematique_parente)
    duplicates = defaultdict(list)
    for obj in SousThematique.objects.all():
        key = (obj.titre.strip().lower(), obj.thematique_parente_id)
        duplicates[key].append(obj)

    # Corriger les doublons de titre en ajoutant un numéro
    for (titre, thematique_id), entries in duplicates.items():
        if len(entries) > 1:
            print(f"⚠️ Doublons trouvés pour '{titre}' (Thématique ID: {thematique_id})")
            for i, obj in enumerate(entries, start=1):
                new_titre = f"{obj.titre} ({i})"
                print(f"  → Mise à jour : {obj.titre} → {new_titre}")
                obj.titre = new_titre
                obj.save()

    # Mettre à jour les slugs
    for obj in SousThematique.objects.all():
        base_slug = slugify(obj.titre)
        unique_slug = base_slug
        counter = 1

        # Vérifier que le slug est unique
        while SousThematique.objects.filter(slug=unique_slug).exclude(id=obj.id).exists():
            unique_slug = f"{base_slug}-{counter}"
            counter += 1
        
        # Mise à jour si nécessaire
        if obj.slug != unique_slug:
            print(f"🔄 Mise à jour du slug : {obj.slug} → {unique_slug}")
            obj.slug = unique_slug
            obj.save()

    print("✅ Tous les titres et slugs ont été mis à jour avec succès !")

if __name__ == "__main__":
    update_titles_and_slugs()
