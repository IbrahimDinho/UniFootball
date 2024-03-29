# Generated by Django 3.1.7 on 2021-05-04 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20210501_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='league',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pages.league'),
        ),
    ]
