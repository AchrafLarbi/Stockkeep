# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from notifications.models import Notification
# from .models import BonDeSortieItem
# from magasinier.middleware import current_request

# @receiver(post_save, sender=BonDeSortieItem)
# def create_notification(sender, instance, created, **kwargs):
#     if created:
#         bon_de_sortie = instance.bon_de_sortie
#         if bon_de_sortie:
#             produit = instance.bon_de_commande_interne_item.produit
#             if produit.quantite_en_stock <= produit.quantite_en_security:
#                 user = current_request().user
#                 Notification.objects.create(
#                     recipient=user,
#                     message=f"Product with id {produit.id} reaches the quantity of security.",
#                     role=user.role,
#                     titre = "Quantity of security"
#                 )
