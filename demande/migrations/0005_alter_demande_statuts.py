# Generated by Django 4.2.1 on 2023-05-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demande', '0004_alter_demande_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='statuts',
            field=models.CharField(choices=[(' traitée', ' traitée'), ('en cours', 'en cours'), ('remis', 'remis')], max_length=200, null=True),
        ),
    ]
