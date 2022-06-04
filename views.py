# from django.shortcuts import render
# from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView

from .models import Element


class HxPageTemplateMixin:
    """Switches template depending on request.htmx"""

    def get_template_names(self):
        if not self.request.htmx:
            return [self.template_name.replace("htmx/", "")]
        else:
            return [self.template_name]


class ElementListView(HxPageTemplateMixin, ListView):
    model = Element
    context_object_name = "elements"
    template_name = "djeotree/htmx/element_list.html"

    def get_queryset(self):
        qs = Element.objects.filter(private=False)
        if self.request.user.is_authenticated:
            qs2 = Element.objects.filter(
                family__user_id=self.request.user.uuid, private=True
            )
            qs = qs | qs2
        return qs
