
```markdown
# Star Buffet - Module de gestion des traiteurs

## Description

Application Django pour la gestion des traiteurs sur la plateforme Star Buffet.

## Prérequis


- Python 3.10+
- MySQL
- asgiref==3.11.1
- Django==6.0.3
- mysqlclient==2.2.8
- python-dotenv==1.2.2
- sqlparse==0.5.5
- Créer et activer un environnement virtuel



## ÉTAPE 1 : Architecture & Modélisation (Le Cœur)

### 1.1 Création du projet et de l'application


django-admin startproject startbuffet_project .
python manage.py startapp services


### 1.2 Configuration de settings.py

Ajouter `'services'` dans `INSTALLED_APPS` :

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'services',  # ← J'ai ajoute l'application services ici
]
```

### 1.3 Création du modèle Traiteur

services/models.py


from django.db import models

class Traiteur(models.Model):
    nom_complet = models.CharField(max_length=50, verbose_name="nom_complet")
    specialites = models.CharField(verbose_name="specialites", max_length=50)
    description = models.TextField(verbose_name="description ")
    adresse = models.CharField(verbose_name="adresse", max_length=50)
    est_actif = models.BooleanField(verbose_name="est_actif", blank=True, null=True, default=True)
    email = models.EmailField(verbose_name="email", max_length=254)
    date_creation = models.DateField(verbose_name="date_creation", auto_now_add=True)
    telephone = models.CharField(verbose_name="telephone", max_length=50)
    image = models.URLField(verbose_name="image", max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.nom_complet} - {self.specialites}"


### 1.4 Enregistrement dans l'admin

services/admin.py


from django.contrib import admin
from .models import Traiteur

@admin.register(Traiteur)
class TraiteurAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'email', 'est_actif')


### 1.5 Migrations

python manage.py makemigrations
python manage.py migrate


## ÉTAPE 2 : Affichage de la liste (/traiteurs/)

### 2.1 Vue liste_traiteurs

services/views.py

from django.shortcuts import render
from .models import Traiteur

def liste_traiteurs(request):
    traiteurs = Traiteur.objects.all()
    return render(request, 'liste.html', {'traiteurs': traiteurs})


### 2.2 Template liste.html

services/templates/liste.html


{% extends "base.html" %}
{% load static %}

{% block title %}Liste des traiteurs{% endblock %}

{% block content %}
{% for t in traiteurs %}
<div class="parent">
    <div class="div4">
        <p>{{ t.nom_complet }}</p>
        <p>Spécialité : {{ t.specialites }}</p>
    </div>
    <div class="div5">
        <button><a href="{% url 'details_traiteur' t.id %}">Voir le profil</a></button>
    </div>
</div>
{% endfor %}
{% endblock %}


### 2.3 Configuration des URLs

services/urls.py


from django.urls import path
from . import views

urlpatterns = [
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('traiteur/', views.liste_traiteurs, name='liste_traiteurs'),
    path('details/<int:id>', views.details_traiteur, name='details_traiteur'),
    path('form/', views.ajoutraiteur, name='ajoutraiteur'),
    path('inscription/', views.SignUpView.as_view(), name='signup'),
]

]


**startbuffet_project/urls.py**


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('services.urls')),
]


## ÉTAPE 3 : Détail dynamique (/traiteurs/<int:id>/detail/)

### 3.1 Vue details_traiteur

**ervices/views.py**

from django.shortcuts import get_object_or_404

def details_traiteur(request, id):
    details = get_object_or_404(Traiteur, pk=id)
    return render(request, 'details.html', {'details': details})
`

### 3.2 Template details.html

**services/templates/details.html**

{% extends "base.html" %}
{% load static %}
{% block title %}details-traiteur{% endblock %}
{% block content %}
{% block extra_css %}<link rel="stylesheet" href="{% static 'services/monstyle.css' %}">{% endblock %}

<body class="bodydetails">
  <section class="section1details">
    <div class="div1section1details">
      <img class="img1detailsection1" src="{% static 'media/plat-prepare-ou-fait-maison-quel-est-le-moins-cher-scaled.jpeg' %}" alt="">
      <div class="verifie">
        <p><i class="fa-solid fa-circle-check"></i> Vérifié</p>
      </div>
      <div class="etoile">
        <p><i class="fa-solid fa-star"></i> 0.0/5</p>
      </div>
    </div>
  </section>

  <section class="section2details">
    <div class="leftsection2details">
      <div class="divleftsection2details">
        <h3>A propos</h3>
        <p>{{ details.nom_complet }}</p>
      </div>

      <div class="divleftsection2details">
        <h3>Contact</h3>
        <p><i class="fa-solid fa-location-dot"></i> {{ details.adresse }}</p>
        <p><i class="fa-solid fa-phone"></i> {{ details.telephone }}</p>
        <p><i class="fa-solid fa-envelope"></i> {{ details.email }}</p>
      </div>

      <div class="divleftsection2details">
        <h3>Spécialité</h3>
        <div class="divSpecialites">
          <p>{{ details.specialites }}</p>
        </div>
      </div>

      <div class="divleftsection2details">
        <h3>Services proposés</h3>
        <div class="divServicesproposes">
          <div>
            <p><i class="fa-solid fa-check"></i> Mariages</p>
            <p><i class="fa-solid fa-check"></i> Cocktails</p>
          </div>
          <div>
            <p><i class="fa-solid fa-check"></i> Anniversaires</p>
            <p><i class="fa-solid fa-check"></i> Cuisine sur mesure</p>
          </div>
        </div>
      </div>

      <div class="divleftsection2details">
        <h3>Expériences</h3>
        <p>19 ans d'expérience</p>
      </div>
    </div>

    <div class="rightsection2details">
      <div class="divrightsection2details">
        <h3>Langues parlées</h3>
        <div class="languesparlees">
          <p>Français</p>
          <p>Indienne</p>
          <p>Arabe</p>
        </div>
      </div>

      <div class="divrightsection2details">
        <button id="contactersection2details">
          <i class="fa-solid fa-phone"></i> Contact
        </button>
      </div>
    </div>
  </section>
</body>

{% endblock %}



## ÉTAPE 4 : Authentification & Sécurité (Login/Logout)

### 4.1 Configuration des URLs d'authentification

**startbuffet_project/urls.py**


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('services.urls')),
]


### 4.2 Configuration des redirections

**startbuffet_project/settings.py**


LOGIN_REDIRECT_URL = 'liste_traiteurs'
LOGOUT_REDIRECT_URL = 'liste_traiteurs'
LOGIN_URL = '/accounts/login'


### 4.3 Template de connexion

**services/templates/registration/login.html**

{% extends 'base.html' %}

{% block title %}Connexion{% endblock %}

{% block content %}
<h2>Connexion</h2>

{% if form.errors %}
<p style="color: red;">Nom d'utilisateur ou mot de passe incorrect.</p>
{% endif %}

<form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td>&nbsp;</td>
            <td><button type="submit">Se connecter</button></td>
        </tr>
    </table>
</form>

<p><a href="{% url 'password_reset' %}">Mot de passe oublié ?</a></p>
<p>Pas encore de compte ? <a href="{% url 'signup' %}">Inscrivez-vous</a></p>
{% endblock %}


### 4.4 Vue d'inscription

**`services/views.py**


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
```

### 4.5 Template d'inscription

**services/templates/registration/signup.html**


{% extends 'base.html' %}

{% block title %}Inscription{% endblock %}

{% block content %}
<h2>Inscription</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">S'inscrire</button>
</form>
{% endblock %}


### 4.6 URL d'inscription

**services/urls.py**


## ÉTAPE 5 : Ajout de contenu (ModelForm)

### 5.1 Création du ModelForm

**services/forms.py**

from django import forms
from .models import Traiteur

class TraiteurForms(forms.ModelForm):
    class Meta:
        model = Traiteur
        fields = '__all__'
        labels = {
            'nom_complet': 'Nom complet',
            'specialites': 'Spécialités culinaires',
            'description': 'Description',
            'adresse': 'Adresse',
            'est_actif': 'Disponibilité',
            'email': 'Email',
            'date_creation': 'Date de création',
            'telephone': 'Téléphone',
            'image': 'URL de l\'image',
        }


### 5.2 Vue avec restriction d'accès pour ajouter un formulaire

**services/views.py**

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import TraiteurForms

@login_required
def ajoutraiteur(request):
    if request.method == 'POST':
        form = TraiteurForms(request.POST)
        if form.is_valid():
            t = form.save()
            return redirect('details_traiteur', id=t.id)
    else:
        form = TraiteurForms()
    return render(request, 'form.html', {'form': form})


### 5.3 Template du formulaire

**ervices/templates/form.html**


{% extends "base.html" %}

{% block title %}Ajouter un traiteur{% endblock %}

{% block content %}
<h1>Ajouter un nouveau traiteur</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Enregistrer</button>
</form>
{% endblock %}


## ÉTAPE 6 : Templates de base (Header, Footer, Base)

### 6.1 Template de base

**templates/base.html**

{% load static %}
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <title>{% block title %}Star Buffet{% endblock %}</title>
    {% block extra_css %}{% endblock %}
</head>
<body>
    {% include "header.html" %}
    {% block content %}{% endblock %}
    {% include "footer.html" %}
</body>
</html>


### 6.2 Header avec navigation et authentification

**templates/header.html**


{% load static %}
<header>
    <nav>
        <div>
            <img src="{% static 'media/logo.png' %}" alt="Logo" class="logo">
        </div>
        <div class="bienvenue">
            <ul>
                <li><a href="{% url 'accueil' %}">Accueil</a></li>
                <li><a href="{% url 'liste_traiteurs' %}">Traiteurs</a></li>
            </ul>
        </div>
        <div class="connect">
            {% if user.is_authenticated %}
                <span>Bonjour, <strong>{{ user.username }}</strong></span>
                <form action="{% url 'logout' %}" method="post">
                    {% csrf_token %}
                    <button type="submit">Déconnexion</button>
                </form>
                <a href="{% url 'ajoutraiteur' %}">Ajouter un traiteur</a>
            {% else %}
                <ul>
                    <li><a href="{% url 'login' %}">Connexion</a></li>
                    <li><a href="{% url 'signup' %}"><button class="inscri">Inscription</button></a></li>
                </ul>
            {% endif %}
        </div>
    </nav>
</header>


### 6.3 Footer

**templates/footer.html**


{% load static %}
<footer>
    <div class="divfooter1">
        <div class="pr">
            <h4>Star Buffet</h4>
            <address>Dakar, Sénégal</address>
            <p>Tel: +221 77 000 00 00</p>
            <p>Email: contact@starbuff.com</p>
        </div>
    </div>
    <div class="soulign">
        <hr>
        <p>© 2025 Star Buffet. Tous droits réservés.</p>
    </div>
</footer>


### 6.4 Page d'accueil

**services/templates/accueil.html**

{% extends "base.html" %}
{% load static %}

{% block title %}Accueil - Star Buffet{% endblock %}

{% block content %}
<section class="sect">
    <div class="left">
        <h1>Découvrez la <span>Cuisine Sénégalaise</span></h1>
        <p>Explorez les saveurs authentiques du Sénégal.</p>
    </div>
</section>

<section class="service">
    <h2>Nos Services</h2>
    <div class="sect2">
        <div class="divsect2">
            <h4>Services de traiteur</h4>
            <p>Organisez vos événements avec nos services de traiteur professionnels.</p>
            <p class="under"><a href="{% url 'liste_traiteurs' %}">Voir les traiteurs →</a></p>
        </div>
    </div>
</section>
{% endblock %}


### 6.5 Vue accueil

**services/views.py**

def accueil(request):
    return render(request, 'accueil.html')


## ÉTAPE 7 : Configuration complète de settings.py

**Fichier : `startbuffet_project/settings.py`**


import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

dbname = os.getenv("DBNAME")
dbuser = os.getenv("DBUSER")
dbpassword = os.getenv("DBPASSWORD")
dbhost = os.getenv("DBHOST")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-votre-cle-secrete'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'services',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'startbuffet_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'startbuffet_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': dbname,
        'USER': dbuser,
        'PASSWORD': dbpassword,
        'HOST': dbhost,
        'PORT': '3306',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'liste_traiteurs'
LOGOUT_REDIRECT_URL = 'liste_traiteurs'
LOGIN_URL = '/accounts/login'


## ÉTAPE 8 : Fichier .env

**.env (à la racine du projet pour cacher les informations de la base de donnee)**

`
DBNAME=star_buffet_db
DBUSER=root
DBPASSWORD=votre_mot_de_passe
DBHOST=localhost


## Installation et exécution

### 1. Installer les dépendances

pip install django mysqlclient 
pip install python-dotenv


### 2. Appliquer les migrations


python manage.py makemigrations
python manage.py migrate


### 3. Créer un superutilisateur

python manage.py createsuperuser


### 4. Lancer le serveur


python manage.py runserver


## Arborescence finale du projet


BriefStarBuffet/
│
├── manage.py
├── .env
├── db.sqlite3
├── InterfaceAdmin.png
│
├── services/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── static/
│   │   └── monstyle.css
│   └── templates/
│       ├── accueil.html
│       ├── details.html
│       ├── form.html
│       ├── liste.html
│       └── registration/
│           ├── login.html
│           └── signup.html
│
├── startbuffet_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── media/
│       ├── banner-caterers.jpg
│       ├── banner-head-accueil.jpg
│       ├── logo.png
│       └── ...
│
└── templates/
    ├── base.html
    ├── header.html
    └── footer.html

## Accès: urls menant aux pages

* Administration : (http://127.0.0.1:8000/admin/)
* Liste des traiteurs : (http://127.0.0.1:8000/traiteur/)
* Ajout d'un traiteur : (http://127.0.0.1:8000/form/)
* details d'un traiteur: (http://127.0.0.1:8000/details/ID)
* Connexion: (http://127.0.0.1:8000/accounts/login/)
* Deconnexion: (http://127.0.0.1:8000/accounts/logout/)
* Inscription: (http://127.0.0.1:8000/inscription/)



## Livrables

-  Code source du projet
-  Capture d'écran interface admin (InterfaceAdmin.png)
-  README.md avec documentation complète



## Auteur
Adji Aissatou Wade SAMBE

