from django.contrib import admin
from .models import Traiteur
# Register your models here.
@admin.register(Traiteur)
class TraiteurAdmin(admin.ModelAdmin):
    list_display= ('nom_complet', 'email', 'est_actif')
    
