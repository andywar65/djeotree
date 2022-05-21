from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from treebeard.mp_tree import MP_Node

User = get_user_model()


class Tag(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_tag",
        verbose_name=_("Author"),
    )
    title = models.CharField(
        _("Title"),
        help_text=_("Tag name"),
        max_length=50,
    )

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        ordering = ("user", "title")

    def __str__(self):
        return self.title


class Family(MP_Node):
    node_order_by = ["title"]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_family",
        verbose_name=_("Author"),
    )
    title = models.CharField(
        _("Title"),
        help_text=_("Family name"),
        max_length=50,
    )
    intro = models.CharField(
        _("Description"),
        null=True,
        blank=True,
        help_text=_("Few words to describe the family"),
        max_length=100,
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name=_("Tags"),
        through="TagValue",
        help_text=_("Choose tags attached to this family"),
    )

    class Meta:
        verbose_name = _("Element Family")
        verbose_name_plural = _("Element Families")

    def __str__(self):
        prefix = ""
        for i in range(self.depth - 1):
            prefix = prefix + "-"
        return prefix + self.title


class TagValue(models.Model):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="tag_value",
        verbose_name=_("Tag"),
    )
    family = models.ForeignKey(
        Family,
        on_delete=models.CASCADE,
        related_name="family_value",
        verbose_name=_("Family"),
    )
    value = models.CharField(
        _("Value"),
        help_text=_("Tag value"),
        max_length=200,
    )

    class Meta:
        verbose_name = _("Tag value")
        verbose_name_plural = _("Tag values")
