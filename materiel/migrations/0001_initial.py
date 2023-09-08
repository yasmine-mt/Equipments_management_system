# Generated by Django 4.2.1 on 2023-05-21 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departement_m', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='materiel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_M', models.CharField(max_length=200, null=True)),
                ('datedereception', models.DateTimeField(auto_now_add=True)),
                ('tag', models.ManyToManyField(to='materiel.tag')),
            ],
        ),
    ]