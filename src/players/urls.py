from django.urls import path

from . import views
# add profile with integer id in this <int:listing_id>
urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logoutUser, name='logout'),
    path('playerstats', views.playerstats , name = 'playerstats'),
    path('team', views.team , name = 'team'),
    path('profile', views.profile , name = 'profile'),

]

# path('<int:playerstat_id>', views.playerstats , name = 'player'),
#     path('<int:team_id>', views.team , name = 'team'),