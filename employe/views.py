from django.shortcuts import render,redirect,HttpResponse
from .models import employe
from .forms import EmployeForm
from demande.filters import DemandeFiltre
from technicien.models import technicien
from demande.models import demande
from materiel.models import materiel
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='acces')
def demandeinfos(request):
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
    return render(request, 'employe/demandeinfos.html', context)
@login_required(login_url='acces')
def list_employe(request,pk):
    Employe=employe.objects.get(id=pk)
    demande=Employe.demande_set.all()
    demande_total=demande.count()
    myFilter=DemandeFiltre(request.GET,queryset=demande )
    demande=myFilter.qs
    context={'Employe':Employe,'demande':demande,'demande_total':demande_total,'myFilter':myFilter}
    return render(request,'employe/list_employe.html',context)
@login_required(login_url='acces')

def creer_employe(request):
    form = EmployeForm()
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('xemploye')
    context = {'form': form}
    return render(request, 'employe/creer_employe.html', context)
@login_required(login_url='acces')

def xemploye(request):
    employes=employe.objects.all()
    context={'employes':employes }
    return render(request,'employe/xemploye.html',context)

@login_required(login_url='acces')
def supprimer_employe(request, pk):
    try:
        employe_obj = employe.objects.get(ID_E=pk)
        if request.method == 'POST':
            employe_obj.delete()
            return redirect('xemploye')
        context = {'item': employe_obj}
        return render(request, 'employe/supprimer_employe.html', context)

    except employe.DoesNotExist:
        return HttpResponse("L'employé spécifié n'existe pas.")