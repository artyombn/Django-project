# Generated by Django 5.0.6 on 2024-07-04 19:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0007_idea_co_author'),
        ('investment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='investors',
            field=models.ManyToManyField(related_name='investors_ideas', through='investment.Investor', to=settings.AUTH_USER_MODEL),
        ),
    ]
