# Generated by Django 3.0.8 on 2020-07-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='title',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]