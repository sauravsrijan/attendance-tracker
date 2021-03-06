# Generated by Django 2.1 on 2018-09-19 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20180918_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='joined',
            new_name='active_from',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='valid_till',
            new_name='active_till',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_active',
        ),
        migrations.AddField(
            model_name='student',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
