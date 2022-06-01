from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Element, ElementTagValue


@receiver(post_save, sender=Element)
def create_element_tags(sender, instance, created, **kwargs):
    if created:
        parent = instance.family
        fam_values = parent.family_value.all()
        for fam_value in fam_values:
            elm_value = ElementTagValue(
                tag_id=fam_value.tag.id, element_id=instance.id, value=fam_value.value
            )
            elm_value.save()
