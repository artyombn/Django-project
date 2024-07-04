# Generated by Django 5.0.6 on 2024-07-04 15:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0006_ideastatus_idea_status'),
        ('partnership', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='co_author',
            field=models.ManyToManyField(related_name='coauthored_ideas', through='partnership.CoAuthor', to=settings.AUTH_USER_MODEL),
        ),
    ]
