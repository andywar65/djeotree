from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import (
    ElementAuthorListView,
    ElementDetailView,
    ElementFamilyListView,
    ElementListView,
)

app_name = "geotree"
urlpatterns = [
    path("", ElementListView.as_view(), name="element_list"),
    path(_("author/<username>"), ElementAuthorListView.as_view(), name="author_list"),
    path(
        _("author/<username>/family/<pk>"),
        ElementFamilyListView.as_view(),
        name="family_list",
    ),
    path(_("element/<pk>"), ElementDetailView.as_view(), name="element_detail"),
]
