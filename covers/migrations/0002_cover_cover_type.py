# Generated by Django 2.0.2 on 2021-09-21 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cover',
            name='cover_type',
            field=models.CharField(choices=[('pianocovers', 'Piano'), ('guitarcovers', 'Guitar')], default='None', max_length=50),
        ),
    ]
