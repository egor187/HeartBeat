# Generated by Django 3.2.4 on 2021-07-18 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heartbeat', '0004_heartbeat_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='team_lead',
        ),
        migrations.DeleteModel(
            name='HeartBeat',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]