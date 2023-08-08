# Generated by Django 4.2.3 on 2023-07-20 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_info_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Pakistan', max_length=99, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(default='https://media.istockphoto.com/id/1337144146/vector/default-avatar-profile-icon-vector.jpg?s=612x612&w=0&k=20&c=BIbFwuv7FxTWvh5S3vB6bkT0Qv8Vn8N5Ffseq84ClGI=', max_length=500)),
                ('name', models.CharField(default='Hazika', max_length=99)),
                ('charges', models.CharField(max_length=200)),
                ('tag', models.CharField(max_length=99)),
                ('rating', models.CharField(default=0.0, max_length=20)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to='App.city')),
                ('field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to='App.field')),
            ],
        ),
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cities', to='App.country'),
        ),
    ]
