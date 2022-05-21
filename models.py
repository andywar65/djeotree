from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from treebeard.mp_tree import MP_Node

User = get_user_model()


class Family(MP_Node):
    node_order_by = ["title"]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_family",
        verbose_name=_("Author"),
    )
    parent = models.ForeignKey(
        "self", verbose_name=_("Parent family"), null=True, on_delete=models.CASCADE
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

    class Meta:
        verbose_name = _("Element Family")
        verbose_name_plural = _("Element Families")

    def __str__(self):
        prefix = ""
        for i in range(self.depth - 1):
            prefix = prefix + "-"
        return prefix + self.title
