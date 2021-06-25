from django.db import models
from datetime import datetime
from django.db.models import Q


class League(models.Model):
    name = models.CharField(max_length=90, unique=True,)

    def __str__(self):
        return self.name


#Team
class Team(models.Model):
    name = models.CharField(max_length=70, unique=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.name

# UNI league table 
class Standing(models.Model):
    
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    won = models.IntegerField()
    loss = models.IntegerField()
    draw = models.IntegerField()
    
    #logic so organiser only inputs win loss or draw and comes out mathmetically correct
    def get_points(self):
        return ((self.won * 3) + self.draw)
    def get_goal_difference(self):
        return (self.goals_for - self.goals_against)
    def get_games_played(self):
        return (self.won + self.loss + self.draw)

    def __str__(self):
        return f"--Team: {self.team.name} --Points: {self.get_points()} --Games played: {self.get_games_played()} --Goal difference: {self.get_goal_difference()}"


# Fixture table
class Fixture(models.Model):
    date_match = models.DateTimeField(default=datetime.now, blank=True) 
    #related name to do the reverse relationship call from team to differentiate between two.
    home_team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name = 'home',)
    away_team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='away',)
    venue = models.CharField(max_length=50)

    compeition_choices = [
        ('League', 'League game'),
        ('Cup', 'Cup game')
    ]
    competition = models.CharField(max_length=30, default='League', choices=compeition_choices)

    def __str__(self):
        return f" on {self.date_match} Match is {self.home_team} VS {self.away_team}"

