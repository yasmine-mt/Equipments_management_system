from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def accesPage(request):
    if request.method == 'POST':
        nom_utilisateur = request.POST.get('nom_utilisateur')
        mot_de_passe = request.POST.get('mot_de_passe')
        user = authenticate(request, username=nom_utilisateur, password=mot_de_passe)
        if user is not None and (user.username == 'Sarah' or user.username == 'Stephanie' or user.username == 'Ahmed' or user.username == 'Sami' or user.username == 'Jamal'):
            messages.error(request, "Désolé, vous n'êtes pas dans l'espace employé.")
        elif user is not None and user.username == 'Superviseur':
            login(request, user)
            return redirect('accueil2')
        elif user is not None and (user.username == 'Mohammed' or user.username == 'Khalid' or user.username == 'Maryam'):
            messages.error(request, "Désolé, vous n'êtes pas dans l'espace technicien.")
        elif user is None:
            messages.error(request, "Utilisateur et/ou mot de passe incorrect(s)")
            return redirect('acces')
    return render(request, 'compte/acces.html')

def accesPage2(request):
    context = {}
    if request.method == 'POST':
        nom_utilisateur = request.POST.get('nom_utilisateur')
        mot_de_passe = request.POST.get('mot_de_passe')
        user = authenticate(request, username=nom_utilisateur, password=mot_de_passe)
        if user is not None and (user.username == 'Sarah' or user.username == 'Stephanie' or user.username == 'Ahmed' or user.username == 'Sami'or user.username == 'Jamal'):
            login(request, user)
            return redirect('accueil')
        elif user is not None and user.username == 'Superviseur':
            messages.error(request, "Désolé, vous n'êtes pas dans l'espace Superviseur.")
        elif user is not None and (user.username == 'Mohammed' or user.username == 'Khalid' or user.username == 'Maryam'):
            messages.error(request, "Désolé, vous n'êtes pas dans l'espace technicien.")
        else:
            messages.error(request, "Utilisateur et/ou mot de passe incorrect(s)")
    context['messages'] = messages.get_messages(request)
    return render(request, 'compte/acces_emp.html', context)

def accesPage3(request):
    context = {}
    if request.method == 'POST':
        nom_utilisateur = request.POST.get('nom_utilisateur')
        mot_de_passe = request.POST.get('mot_de_passe')
        user = authenticate(request, username=nom_utilisateur, password=mot_de_passe)
        if user is not None and (user.username == 'Sarah' or user.username == 'Stephanie' or user.username == 'Ahmed'or user.username == 'Sami'or user.username == 'Jamal'):
            messages.error(request, "Désolé, vous n'êtes pas dans l'espace employé.") 
        elif user is not None and user.username == 'Superviseur':
            messages.error(request, "Désolé, vous n'êtes pas dans l'espace Superviseur.")
        elif user is not None and (user.username == 'Mohammed' or user.username == 'Khalid' or user.username == 'Maryam'):
            login(request, user)
            return redirect('accueil_technicien')
        else:
            messages.error(request, "Utilisateur et/ou mot de passe incorrect(s)")
    context['messages'] = messages.get_messages(request)
    return render(request, 'compte/acces_tech.html', context)



def choix_espace(request):
    espace = request.GET.get('espace')
    if espace == 'employe':
        # Logique de redirection vers l'espace employé
        return redirect('acces_emp')
    elif espace == 'technicien':
        # Logique de redirection vers l'espace technicien
        return redirect('acces_tech')
    elif espace == 'superviseur':
        # Logique de redirection vers l'espace superviseur
        return redirect('acces')
    else:
        # Redirection par défaut ou gestion d'une sélection invalide
        return redirect('choix_espace')



def logoutUser(request):
    logout(request)
    return redirect('/')