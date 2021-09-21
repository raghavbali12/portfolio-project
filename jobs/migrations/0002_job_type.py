# Generated by Django 2.0.2 on 2021-09-21 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='type',
            field=models.CharField(choices=[('pianocover', 'Piano cover'), ('guitarcover', 'Guitar cover'), ('project', 'Coding project')], default='project', max_length=50),
        ),
    ]