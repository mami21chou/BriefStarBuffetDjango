from .models import Traiteur
from django import forms

class TraiteurForms(forms.ModelForm):
    class Meta:
        model=Traiteur
        fields= '__all__'
        labels={
            'nom_complet':'nom complet',
            'specialites':'Specialite, culinaires',
            'description':'description',
            'adresse': 'adresse traiteur',
            'est_actif':'disponibilite traiteur',
            'email':'email traiteur',
            'date_creation': 'date',
            'telephone':'numero telephone',
            'image': 'url de limage',

        }   
        
