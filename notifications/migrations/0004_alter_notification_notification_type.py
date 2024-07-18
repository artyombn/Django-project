# Generated by Django 5.0.6 on 2024-07-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_alter_notification_notification_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.IntegerField(choices=[(1, 'LikeIdea'), (2, 'DisLikeIdea'), (3, 'Comment'), (4, 'Follow'), (5, 'CoAuthorRequest'), (6, 'CoAuthorApproved'), (7, 'CoAuthorRejected'), (8, 'CoAuthorStopped'), (9, 'IdeaFollowed'), (10, 'Investor')]),
        ),
    ]
