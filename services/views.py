from django.shortcuts import render, get_object_or_404, redirect
from .models import Traiteur
from .forms import TraiteurForms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.

def liste_traiteurs(request):
    traiteurs= Traiteur.objects.all()
    return render(request, 'liste.html', {'traiteurs':traiteurs})



def details_traiteur(request,id):
    details=get_object_or_404(Traiteur,pk=id)
    return render(request,'details.html', {'details':details})

@login_required
def ajoutraiteur(request):
    if request.method=='POST':
        form=TraiteurForms(request.POST)
        if form.is_valid():
            t=form.save()
            return redirect('details_traiteur', id=t.id)
           

    else:
        form=TraiteurForms()
    return render(request, 'form.html', {'form':form} )   




class SignUpView(CreateView):
    form_class= UserCreationForm
    success_url= reverse_lazy('login')
    template_name= 'registration/signup.html'
    