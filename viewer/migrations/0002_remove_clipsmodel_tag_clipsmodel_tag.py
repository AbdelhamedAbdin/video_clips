# Generated by Django 4.1.3 on 2022-11-21 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clipsmodel',
            name='tag',
        ),
        migrations.AddField(
            model_name='clipsmodel',
            name='tag',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='viewer.tagsmodel'),
        ),
    ]
