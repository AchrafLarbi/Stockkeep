# Generated by Django 4.2.4 on 2024-06-04 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Service_Achat', '0001_initial'),
        ('consommateur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_bon', models.CharField(blank=True, max_length=255, null=True)),
                ('quantite_sortie', models.IntegerField(blank=True, null=True)),
                ('consommateur', models.CharField(blank=True, max_length=255, null=True)),
                ('observations', models.TextField(blank=True, null=True)),
                ('date_sortie', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BonDeReception',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('facture', models.FileField(blank=True, null=True, upload_to='pdfs/')),
                ('bon_de_commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='Service_Achat.bondecommande')),
            ],
        ),
        migrations.CreateModel(
            name='BonDeSortie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('type', models.CharField(choices=[('Supply', 'Supply'), ('Decharge', 'Decharge')], max_length=40)),
                ('bon_de_commande_interne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consommateur.bondecommandeinterne')),
            ],
        ),
        migrations.CreateModel(
            name='FicheMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produit_id', models.IntegerField()),
                ('date_entree', models.DateField(blank=True, null=True)),
                ('fournisseur', models.CharField(blank=True, max_length=255)),
                ('quantite_entree', models.IntegerField(blank=True, null=True)),
                ('sum_quantite_sortie', models.IntegerField(blank=True, null=True)),
                ('reste', models.IntegerField(blank=True, null=True)),
                ('additional_info', models.ManyToManyField(blank=True, to='magasinier.additionalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='EtatInventaireProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N_inventaire', models.CharField(max_length=255)),
                ('reste', models.IntegerField(default=0)),
                ('quantite_entree', models.IntegerField(default=0)),
                ('quantite_sortie', models.IntegerField(default=0)),
                ('quantite_physique', models.IntegerField(default=0)),
                ('quantite_logique', models.IntegerField(default=0)),
                ('observation', models.TextField(blank=True)),
                ('ecrat', models.IntegerField(blank=True)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produ', to='Service_Achat.produit')),
            ],
        ),
        migrations.CreateModel(
            name='EtatInventaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('etat', models.CharField(choices=[('Approuved', 'Approuved'), ('Not Approuved', 'Non Approuved')], max_length=150)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etat_inventaires_art', to='Service_Achat.article')),
                ('chapitre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etat_inventaires_chap', to='Service_Achat.chapitre')),
                ('produits', models.ManyToManyField(related_name='etatinventaire', to='magasinier.etatinventaireproduit')),
            ],
        ),
        migrations.CreateModel(
            name='BonDeSortieItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite_accorde', models.IntegerField()),
                ('observation', models.TextField(blank=True)),
                ('bon_de_commande_interne_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bondesortie_item', to='consommateur.bondecommandeinterneitem')),
                ('bon_de_sortie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='magasinier.bondesortie')),
            ],
        ),
        migrations.CreateModel(
            name='BonDeReceptionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_produit', models.CharField(max_length=255)),
                ('quantite_commandee', models.PositiveIntegerField(null=True)),
                ('quantite_livree', models.PositiveIntegerField(null=True)),
                ('reste_a_livrer', models.PositiveIntegerField(null=True)),
                ('bon_de_reception', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='magasinier.bondereception')),
            ],
        ),
    ]