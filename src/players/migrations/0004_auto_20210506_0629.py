# Generated by Django 3.1.7 on 2021-05-06 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_playerprofile_assists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerprofile',
            name='appereances',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='playerprofile',
            name='assists',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='playerprofile',
            name='goals',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='playerprofile',
            name='red_card',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='playerprofile',
            name='yellow_card',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]