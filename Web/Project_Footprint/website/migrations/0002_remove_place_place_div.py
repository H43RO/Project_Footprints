# Generated by Django 3.0.8 on 2020-07-26 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='place_div',
        ),
    ]