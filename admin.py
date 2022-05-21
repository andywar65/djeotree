from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Family, Tag


class FamilyAdmin(TreeAdmin):
    form = movenodeform_factory(Family)

    fieldsets = (
        (
            None,
            {
                "fields": ("user", "title", "intro"),
            },
        ),
        (
            None,
            {
                "fields": ("_position", "_ref_node_id"),
            },
        ),
    )


admin.site.register(Family, FamilyAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title",)
