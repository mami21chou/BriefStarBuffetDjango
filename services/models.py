from django.db import models

# Create your models here.


# Dans models.py, créer une classe Traiteur avec : nomcomplet (CharField), 
# specialites, description (TextField), adresse (CharField), est-actif(BooleanField) 
# email(EmailField)) , datedecreation (DateTimeField), telephone (CharField), image (URLField - optionnel)_



class Traiteur(models.Model):
    nom_complet=models.CharField(max_length=50, verbose_name="nom_complet")
    specialites= models.CharField(verbose_name="specialites", max_length=50)
    description= models.TextField(verbose_name="description ")
    adresse=models.CharField(verbose_name="adresse", max_length=50)
    est_actif=models.BooleanField(verbose_name="est_actif", blank=True, null=True, default=True)
    email=models.EmailField(verbose_name="email", max_length=254)
    date_creation=models.DateField(verbose_name="date_creation", auto_now=False, auto_now_add=True)
    telephone=models.CharField(verbose_name="telephone", max_length=50)
    image= models.URLField(verbose_name="image", max_length=200, null=True, blank=True)


def __str__(self):
    return f"{self.nom_complet} - {self.specialites} - {self.est_actif}"
