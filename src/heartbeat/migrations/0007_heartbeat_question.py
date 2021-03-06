# Generated by Django 3.2.4 on 2021-07-19 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('heartbeat', '0006_auto_20210719_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text of the question')),
                ('team_lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('text', 'team_lead')},
            },
        ),
        migrations.CreateModel(
            name='HeartBeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('yesterday_plan', models.TextField()),
                ('today_plan', models.TextField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='heartbeats', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='heartbeats', to='heartbeat.question')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heartbeats', to='heartbeat.team')),
            ],
        ),
    ]
