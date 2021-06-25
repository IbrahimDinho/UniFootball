from django.db import models
from django.contrib.auth.models import User
from pages.models import Team
# Create your models here.

class PlayerProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    appereances = models.IntegerField(default=0, null=True, blank=True)
    goals = models.IntegerField(default=0, null=True, blank=True)
    assists = models.IntegerField(default=0, null=True, blank=True)
    yellow_card = models.IntegerField(default=0, null=True, blank=True)
    red_card = models.IntegerField(default=0, null=True, blank=True)

    position_choices = [
        ('Manager', 'Manager'),
        ('Forward', 'Forward'),
        ('GK', 'GoalKeeper'),
        ('MID', 'Midfielder'),
        ('Defence', 'Defender'),
    ]
    
    football_position = models.CharField(max_length=30, choices=position_choices)
    #may need to make photos folder and manage.py collectstatic command.
    profile_picture = models.ImageField(upload_to='photos/', null=True, blank=True) 
    motm = models.BooleanField(default=False, null=True, blank=True)

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # class Meta:
    #     constraints = [models.UniqueConstraint(fields=['user.username', 'email'], name='unique_user')]
    
    def __str__(self):
        return self.user.username