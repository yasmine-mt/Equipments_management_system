# Generated by Django 4.2.1 on 2023-06-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demande', '0019_alter_demande_employe_alter_demande_materiel'),
    ]

    operations = [
        migrations.AddField(
            model_name='demande',
            name='demandes_assignees',
            field=models.ManyToManyField(blank=True, related_name='assignees', to='demande.demande'),
        ),
    ]
