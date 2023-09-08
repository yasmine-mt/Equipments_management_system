
from django.shortcuts import render, redirect
from employe.models import employe
from django.http import HttpResponse
from materiel.models import materiel
from technicien.models import technicien
from .models import demande
from .forms import DemandeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='acces')
def list_demande(request):
    return render(request,'demande/list_demande.html')

@login_required(login_url='acces')
def xdemande(request):
    demandes=demande.objects.all()
    employes=employe.objects.all()
    materiels = materiel.objects.all()
    context={'demandes':demandes , 'employes':employes, 'materiels':materiels}
    return render(request,'demande/xdemande.html',context)
@login_required(login_url='acces')
def volet_view(request):
    return render(request, 'demande/volet.html')
@login_required(login_url='acces')
def demande_reparation(request):
    demandes=demande.objects.all()
    context={'demandes':demandes }
    return render(request,'demande/demande_reparation.html',context)
@login_required(login_url='acces')
def demande_attribution(request):
    demandes=demande.objects.all()
    context={'demandes':demandes }
    return render(request,'demande/demande_attribution.html',context)
@login_required(login_url='acces')
def dt(request):
    techniciens = technicien.objects.filter(statuts='Libre')
    demandes = demande.objects.filter(type=' Réparation',statuts='non traitée')
    context = {'techniciens': techniciens,'demandes': demandes}
    return render(request, 'demande/confirmation.html', context)
@login_required(login_url='acces')
def attribuer_materiel_employe(request, demande_id):
    try:
        print("Demande ID:", demande_id)  # Ajout d'une impression pour vérifier la valeur de demande_id

        demande_obj = demande.objects.get(ID_D=demande_id)

        print("Demande trouvée:", demande_obj)  # Ajout d'une impression pour vérifier la demande récupérée


        if demande_obj.statuts == 'non traitée' and demande_obj.type == 'Attribution':
            demande_obj.statuts = ' traitée'
            demande_obj.save()

            return  HttpResponse("La demande est traitée")
        else:
            return HttpResponse("Une erreur s'est produite lors de l'attribution du matériel à l'employé.")
    except demande.DoesNotExist:
        return HttpResponse("La demande spécifiée n'existe pas.")


@login_required(login_url='acces')
def assigner_untec(request, demande_id, technicien_id):
    try:
        demande_obj = demande.objects.get(ID_D=demande_id)
        technicien_obj = technicien.objects.get(ID_T=technicien_id)

        if demande_obj.statuts == 'non traitée' and demande_obj.type == ' Réparation' and technicien_obj.statuts == 'Libre':
            demande_obj.statuts = 'en cours'
            demande_obj.technicien = technicien_obj
            demande_obj.save()

            technicien_obj.demandes_assignees.add(demande_obj)
            technicien_obj.statuts = 'Assigné'
            technicien_obj.save()

        techniciens_assignes = technicien.objects.filter(demandes_assignees__isnull=False)
        demandes_assignees = demande.objects.filter(technicien__in=techniciens_assignes)

        context = {
            'demandes_assignees': demandes_assignees
        }

        return render(request, 'demande/Assignation.html', context)
    except demande.DoesNotExist:
        return HttpResponse("La demande spécifiée n'existe pas.")
def demandesass(request):
    techniciens_assignes = technicien.objects.filter(demandes_assignees__isnull=False)
    demandes_assignees = demande.objects.filter(technicien__in=techniciens_assignes)

    context = {
        'demandes_assignees': demandes_assignees
    }

    return render(request, 'demande/Assignation.html', context)
def ajouter_demande(request):
    form = DemandeForm()
    if request.method == 'POST':
        form = DemandeForm(request.POST)
        if form.is_valid():
            demande = form.save(commit=False)
            demande.save()
            return redirect('accueil')
    context = {'form': form}
    return render(request, 'demande/ajouter_demande.html', context)

def supprimer_demande(request, demande_id):
    try:
        demande_obj = demande.objects.get(ID_D=demande_id)
        demande_obj.delete()
        return HttpResponse("La demande est supprimée avec succès.")
    except demande.DoesNotExist:
        return HttpResponse("La demande spécifiée n'existe pas.")