# Generated by Django 4.2.3 on 2023-07-17 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='Hazika', max_length=99),
        ),
    ]