# Generated by Django 3.2.4 on 2021-07-21 12:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('heartbeat', '0008_rename_member_heartbeat_creator'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='team',
            unique_together={('name', 'team_lead')},
        ),
    ]
