from django.shortcuts import render

from .models import Team, Standing, Fixture, League

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def table(request):
    if Standing:
        return render(request, 'pages/table.html')
    all_team_table = Standing.objects.all()
    leagues = League.objects.all()
    
    #Check user logged in
    if request.user.is_authenticated:
        #get league user plays in
        league_user_plays = request.user.playerprofile.team.league.name
        #get table for all teams
        #filter to get table for league of user
        table = all_team_table.filter(team__league__name=league_user_plays)
        table_order = table.order_by('-won', '-draw', '-goals_for', 'goals_against')
    else:
        #if user not logged in show first league by default
        leagues_first = leagues.first().name
        team_in_league = all_team_table.filter(team__league__name=leagues_first)
        # minus is for descending order 
        table_order = team_in_league.order_by('-won', '-draw', '-goals_for', 'goals_against')
    #if user, logged in or not, submits form to change league 
    if request.method == 'POST':
        #get league name from form submitted
        league_value = request.POST.get('league')
        print(league_value)
        table = all_team_table.filter(team__league__name=league_value)
        table_order = table.order_by('-won', '-draw', '-goals_for', 'goals_against')

        context = {'table': table_order, 'leagues': leagues, 'selectedleague': league_value}
        return render(request, 'pages/table.html', context)

    context = {'table': table_order, 'leagues': leagues}
    
    return render(request, 'pages/table.html', context)


def fixtures(request):
    fixtures = Fixture.objects.all()
    fixture_order = fixtures.order_by('date_match')
    context = {'fixture': fixture_order}
    return render(request, 'pages/fixtures.html', context )

def premierLeague(request):
    return render(request, 'pages/premierleague.html')

def quiz(request):
    return render(request, 'pages/quiz.html')

def quizq(request):
    return render(request, 'pages/quizq.html')

def quizend(request):
    return render(request, 'pages/quizend.html')

