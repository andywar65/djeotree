from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Element


@receiver(post_save, sender=Element)
def create_element_tags(sender, instance, created, **kwargs):
    if created:
        pass
