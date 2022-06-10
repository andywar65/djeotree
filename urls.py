from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import ElementRedirectView  # noqa
from .views import (
    BaseListView,
    ElementAuthorListView,
    ElementDetailView,
    ElementFamilyListView,
    ElementListView,
)

app_name = "geotree"
urlpatterns = [
    path("", BaseListView.as_view(), name="base_list"),
    path(_("authors"), ElementListView.as_view(), name="element_list"),
    path(_("author/<username>"), ElementAuthorListView.as_view(), name="author_list"),
    path(
        _("authors/<username>/family/<pk>"),
        ElementFamilyListView.as_view(),
        name="family_list",
    ),
    path(
        _("author/<username>/element/<pk>"),
        ElementDetailView.as_view(),
        name="element_detail",
    ),
]
