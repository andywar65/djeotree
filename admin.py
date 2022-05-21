from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Family, Tag, TagValue


class TagValueInline(admin.TabularInline):
    model = TagValue
    fields = ("tag", "value")
    extra = 0


class FamilyAdmin(TreeAdmin):
    form = movenodeform_factory(Family)
    inlines = [
        TagValueInline,
    ]

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
