from django.shortcuts import render
from demande.models import demande
from employe.models import employe
from technicien.models import technicien
from .models import materiel
from django.shortcuts import redirect
from .forms import MaterielForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='acces')
def home(request):
    employe_nom = request.user.username
    employe_obj = employe.objects.get(nomE=employe_nom)

    demandes = demande.objects.filter(employe=employe_obj)  # Filtrer les demandes par l'employé
    demande_total = demandes.count() if demandes else 0  # Vérifier si la liste de demandes est vide

    employes = employe.objects.all()
    techniciens = technicien.objects.all()
    materiels = materiel.objects.all()

    context = {
        'employe': employe_obj,  # Ajouter l'objet employé à context
        'demandes': demandes,
        'employes': employes,
        'demande_total': demande_total,
        'techniciens': techniciens,
        'materiels': materiels
    }
    return render(request, 'materiel/accueil.html', context)
def dashboard(request):
    # Fetching the data for the dashboard
    demandes = demande.objects.all()
    employes = employe.objects.all()
    techniciens = technicien.objects.all()
    materiels = materiel.objects.all()

    total_employes = employes.count()
    total_techniciens_libres = techniciens.filter(statuts='Libre').count()
    total_techniciens_assignes = techniciens.filter(statuts='Assigné').count()
    total_demandes_non_traites = demandes.filter(statuts='non traitée').count()

    # Fetching the latest employees added recently
    derniers_demandes = demandes.order_by('-date_creation')[:3]
 

    context = {
        'demandes': demandes,
        'employes': employes,
        'total_employes': total_employes,
        'total_techniciens_libres': total_techniciens_libres,
        'total_techniciens_assignes': total_techniciens_assignes,
        'total_demandes_non_traites': total_demandes_non_traites,
        'techniciens': techniciens,
        'materiels': materiels,
        'derniers_demandes': derniers_demandes
    }
    return render(request, 'materiel/dashboard.html', context)



def accueil(request):
    return render(request,'materiel/Home.html')
@login_required(login_url='acces')
def accueil2(request):

    demandes = demande.objects.all
    employes = employe.objects.all()
    techniciens = technicien.objects.all()
    materiels = materiel.objects.all()

    context = {
        'employes': employes,
        'demandes': demandes,
        'employes': employes,
        'techniciens': techniciens,
        'materiels': materiels
    }
    return render(request, 'materiel/accueil2.html', context)

#@login_required(login_url='acces')
@login_required(login_url='acces')
def home_technicien(request):
        return render(request, 'materiel/accueil_technicien.html')
@login_required(login_url='acces')
def technique(request):
    technicien_obj = technicien.objects.get(Nom=request.user.username)
    demandes_assignees = technicien_obj.demandes_assignees.all()

    context = {
        'technicien': technicien_obj,
        'demandes_assignees': demandes_assignees
    }
    return render(request, 'materiel/infotechnicien.html', context)
@login_required(login_url='acces')
def signaler_reparation(request, demande_id):
    Demande = demande.objects.get(ID_D=demande_id)
    Demande.statuts = 'traitée'
    Demande.save()

    technicien = Demande.techniciens_assignes.first()
    technicien.statuts = 'Libre'
    technicien.save()

    return redirect('accueil_technicien')

@login_required(login_url='acces')
def enregistrer_materiel(request):
    form = MaterielForm()  
    if request.method == 'POST':
        form = MaterielForm(request.POST)
        if form.is_valid():
            materiel = form.save(commit=False)
            materiel.save()
            return redirect('xmateriel')
    context = {'form': form}
    return render(request, 'materiel/enregistrer_materiel.html', context)
@login_required(login_url='acces')

def xmateriel(request):
    materiels=materiel.objects.all()
    context={'materiels':materiels }
    return render(request,'materiel/xmateriel.html',context)


