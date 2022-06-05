from django.contrib.auth import get_user_model
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView

from .models import Element, Family

# from django.shortcuts import render
# from django.utils.translation import gettext_lazy as _


User = get_user_model()


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors = Family.objects.values_list("user__username", flat=True)
        authors = list(dict.fromkeys(authors))
        context["authors"] = authors
        # TODO if only one author skips to ElementAuthorListView
        return context


class ElementAuthorListView(HxPageTemplateMixin, ListView):
    model = Element
    context_object_name = "elements"
    template_name = "djeotree/htmx/element_author_list.html"

    def setup(self, request, *args, **kwargs):
        super(ElementAuthorListView, self).setup(request, *args, **kwargs)
        self.author = get_object_or_404(User, username=self.kwargs["username"])

    def get_queryset(self):
        qs = Element.objects.filter(family__user_id=self.author.uuid, private=False)
        if self.request.user.is_authenticated:
            qs2 = Element.objects.filter(
                family__user_id=self.request.user.uuid, private=True
            )
            qs = qs | qs2
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        families = Family.objects.filter(user_id=self.author.uuid)
        context["families"] = families
        context["author"] = self.author
        return context


class ElementFamilyListView(HxPageTemplateMixin, ListView):
    model = Element
    context_object_name = "elements"
    template_name = "djeotree/htmx/element_family_list.html"

    def setup(self, request, *args, **kwargs):
        super(ElementFamilyListView, self).setup(request, *args, **kwargs)
        self.author = get_object_or_404(User, username=self.kwargs["username"])
        self.family = get_object_or_404(Family, id=self.kwargs["pk"])
        if not self.author == self.family.user:
            raise Http404(_("Family does not belong to User"))

    def get_queryset(self):
        qs = Element.objects.filter(family_id=self.family.id, private=False)
        if self.request.user.is_authenticated:
            qs2 = Element.objects.filter(family_id=self.family.id, private=True)
            qs = qs | qs2
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["family"] = self.family
        context["author"] = self.author
        return context


class ElementDetailView(HxPageTemplateMixin, DetailView):
    model = Element
    context_object_name = "element"
    template_name = "djeotree/htmx/element_detail.html"

    def get_object(self, queryset=None):
        super(ElementDetailView, self).get_object(queryset=None)
        self.family = self.object.family
        self.author = self.family.user
        if self.object.private and self.author != self.request.user:
            return HttpResponseForbidden()
