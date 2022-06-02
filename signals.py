from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Element, ElementTagValue, TagValue


@receiver(post_save, sender=Element)
def create_element_tags(sender, instance, created, **kwargs):
    if created:
        parent = instance.family
        # get parent ancestors and generate element tag values
        ancestors = parent.get_ancestors()
        for ancestor in ancestors:
            fam_values = TagValue.objects.filter(family_id=ancestor.id)
            for fam_value in fam_values:
                elm_value = ElementTagValue(
                    tag_id=fam_value.tag.id,
                    element_id=instance.id,
                    value=fam_value.value,
                )
                elm_value.save()
        # generate element tag values from parent
        fam_values = TagValue.objects.filter(family_id=parent.id)
        for fam_value in fam_values:
            elm_value = ElementTagValue(
                tag_id=fam_value.tag.id, element_id=instance.id, value=fam_value.value
            )
            elm_value.save()
