from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('traiteur/', views.liste_traiteurs, name='liste_traiteurs'),
    path('details/<int:id>', views.details_traiteur, name='details_traiteur'),
    path('form/', views.ajoutraiteur, name='ajoutraiteur'),
    path('inscription/', views.SignUpView.as_view(), name="signup"),
    path('', views.accueil, name='accueil')
]