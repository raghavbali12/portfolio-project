# Generated by Django 3.2.9 on 2021-11-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20210921_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(choices=[('pianocovers', 'Piano cover'), ('guitarcovers', 'Guitar cover'), ('allblogs', 'Blog')], default='pianocover', max_length=50),
        ),
    ]
