# Generated by Django 4.2.4 on 2024-06-04 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BonDeCommandeInterne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Created succesfully', 'Created succesfully'), ('Validated by the responsable', 'Validated by the responsable'), ('Validated by the director', 'Validated by the director'), ('Delivered', 'Delivered'), ('External Discharge', 'External Discharge')], max_length=40)),
                ('type', models.CharField(choices=[('Supply', 'Supply'), ('Decharge', 'Decharge')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='BonDeCommandeInterneItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite_demandee', models.PositiveIntegerField(null=True)),
                ('quantite_accorde', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]