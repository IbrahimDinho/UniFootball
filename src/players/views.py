from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, PlayerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import PlayerProfile
from pages.models import Team
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    #once user logged in can't go to register page
    if request.user.is_authenticated:
        return redirect('index')
    else: 
        form = CreateUserForm()
        profile_form = PlayerForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            profile_form = PlayerForm(request.POST)
            print(profile_form)
            # form validation returning error messages
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1']
            password2 = request.POST['password2']
            if password != password2 :
                messages.error(request, 'Passwords do not match')
                return redirect('register')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email already in use')
                return redirect('register')

            if form.is_valid() and profile_form.is_valid():
                user = form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')

                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('index')
            else:
                messages.error(request,'Please fill out all fields and make sure password long enough')
                return redirect('register')     

        context = {'form': form, 'profile_form': profile_form}
        return render(request, 'players/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index') 
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
        return render(request, 'players/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

#restrict the views below must be logged in.
@login_required(login_url='login')
def playerstats(request):
    team_user_plays = request.user.playerprofile.team
    #all players for given user
    team_players = team_user_plays.playerprofile_set.all()
    team_players_sorted = team_players.order_by('-appereances')

    context = {'table' : team_players_sorted}
    return render(request, 'players/playerstat.html', context)

@login_required(login_url='login')
def team(request):
    team_user_plays = request.user.playerprofile.team
    team_players = team_user_plays.playerprofile_set.all()

    #split into Manager, attack,def ,mid 
    managers = team_players.filter(football_position='Manager')
    attackers = team_players.filter(football_position='Forward')
    goalkeepers = team_players.filter(football_position='GK')
    midfielders = team_players.filter(football_position='Mid')
    defenders = team_players.filter(football_position='Defence')
    motm = team_players.filter(motm = True)
    context = {'managers': managers, 'attackers': attackers, 'goalkeepers' : goalkeepers, 'midfielders' : midfielders, 'defenders': defenders, 'motm' : motm}
    return render(request, 'players/team.html', context)

@login_required(login_url='login')
def profile(request):
    player = request.user.playerprofile
    form = PlayerForm(instance=player)

    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'players/profile.html', context)

