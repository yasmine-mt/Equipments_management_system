from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TechnicienForm
from.models import technicien
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='acces')

def list_technicien(request):
    return render(request,'technicien/list_technicien.html')
@login_required(login_url='acces')

def ajouter_technicien(request):
     form=TechnicienForm()
     if request.method=='POST':
        form=TechnicienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('xtechnicien')
     context={'form':form}
     return render(request,'technicien/ajouter_technicien.html',context
                   )
@login_required(login_url='acces')

def xtechnicien(request):
    techniciens=technicien.objects.all()
    context={'techniciens':techniciens }
    return render(request,'technicien/xtechnicien.html',context)
@login_required(login_url='acces')
def supprimer_technicien(request, pk):
    try:
        technicien_obj = technicien.objects.get(ID_T=pk)

        if request.method == 'POST':
            # Vérifier si le technicien est assigné à des demandes
            demandes_assignees = technicien_obj.demandes_assignees.all()

            if demandes_assignees.exists():
                # Désassigner le technicien des demandes assignées
                for demande_obj in demandes_assignees:
                    demande_obj.technicien = None
                    demande_obj.statuts = 'non traitée'
                    demande_obj.save()

            technicien_obj.delete()
            return redirect('xtechnicien')


        context = {'item': technicien_obj}
        return render(request, 'technicien/supprimer_technicien.html', context)

    except technicien.DoesNotExist:
        return HttpResponse("Le technicien spécifié n'existe pas.")


