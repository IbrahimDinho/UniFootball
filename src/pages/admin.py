from django.contrib import admin
from .models import Team, Standing, Fixture, League
from django.contrib.auth.models import Group
# Register your models here.

# Decorater method to register on admin.
@admin.register(Standing)
class StandingAdmin(admin.ModelAdmin):
    list_display = ('team','Points','won', 'draw', 'loss', 'goal_difference','goals_for', 'goals_against','league_play_in')
    list_editable = ('won', 'draw', 'loss', 'goals_for', 'goals_against',)
    def Points(self, obj):
        return obj.get_points()

    def goal_difference(self,obj):
        return obj.get_goal_difference() 
    
    def league_play_in(self,obj):
        return obj.team.league
   
    Points.admin_order_field = '_Points'

@admin.register(Fixture)
class FixtureAdmin(admin.ModelAdmin):
    list_display = ('home_team','away_team','venue','competition','date_match')
    list_display_links= ('home_team','away_team')
    list_editable = ('venue','competition')


#django login page customisation
admin.site.site_header = "Login to UniFootball Admin Page"
admin.site.site_title = "UniFootball Admin"
admin.site.index_title = "Welcome to UniFootball Admin Page to organise the League"


admin.site.unregister(Group)
admin.site.register(Team)
admin.site.register(League)
# admin.site.register(Standing, StandingAdmin)
# admin.site.register(Fixture)