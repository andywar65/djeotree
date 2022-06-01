from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Element, ElementImage, ElementTagValue, Family, Tag, TagValue


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


class ElementImageInline(admin.TabularInline):
    model = ElementImage
    fields = (
        "position",
        "description",
        "fb_image",
    )
    sortable_field_name = "position"
    extra = 0


class ElementTagValueInline(admin.TabularInline):
    model = ElementTagValue
    fields = ("tag", "value")
    extra = 0


class ElementAdmin(LeafletGeoAdmin):
    list_display = ("__str__",)
    inlines = [
        ElementImageInline,
        ElementTagValueInline,
    ]


admin.site.register(Element, ElementAdmin)
