from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import (
    AuthorDetailView,
    AuthorListView,
    BaseListView,
    ElementCreateView,
    ElementDayArchiveView,
    ElementDeleteView,
    ElementDetailView,
    ElementMonthArchiveView,
    ElementUpdateView,
    ElementYearArchiveView,
    FamilyDetailView,
    FamilyListView,
    ImageCreateView,
    ImageDeleteView,
    ImageDetailView,
    ImageLoopView,
    ImageUpdateView,
    TagDetailView,
    TagListView,
    ValueCreateView,
    ValueDeleteView,
    ValueDetailView,
    ValueUpdateView,
    family_element_download,
)

app_name = "geotree"
urlpatterns = [
    path("", BaseListView.as_view(), name="base_list"),
    path(_("families/"), FamilyListView.as_view(), name="family_list"),
    path(_("authors/"), AuthorListView.as_view(), name="author_list"),
    path(_("tags/"), TagListView.as_view(), name="tag_list"),
    path(_("family/<pk>/"), FamilyDetailView.as_view(), name="family_detail"),
    path(_("family/<pk>/download/"), family_element_download, name="family_download"),
    path(_("author/<username>/"), AuthorDetailView.as_view(), name="author_detail"),
    path(_("tag/<pk>/"), TagDetailView.as_view(), name="tag_detail"),
    path(
        _("author/<username>/element/add/"),
        ElementCreateView.as_view(),
        name="element_create",
    ),
    path(
        _("author/<username>/element/<pk>/"),
        ElementDetailView.as_view(),
        name="element_detail",
    ),
    path(
        _("author/<username>/element/<pk>/change/"),
        ElementUpdateView.as_view(),
        name="element_update",
    ),
    path(
        _("author/<username>/element/<pk>/delete/"),
        ElementDeleteView.as_view(),
        name="element_delete",
    ),
    path(
        "<int:year>/",
        ElementYearArchiveView.as_view(),
        name="year_detail",
    ),
    path(
        "<int:year>/<int:month>/",
        ElementMonthArchiveView.as_view(),
        name="month_detail",
    ),
    path(
        "<int:year>/<int:month>/<int:day>/",
        ElementDayArchiveView.as_view(),
        name="day_detail",
    ),
    # used for inlines
    path(_("element/<pk>/images/"), ImageLoopView.as_view(), name="image_loop"),
    path(_("element/<pk>/image/add/"), ImageCreateView.as_view(), name="image_create"),
    path(_("element/image/<pk>/"), ImageDetailView.as_view(), name="image_detail"),
    path(
        _("element/image/<pk>/change/"), ImageUpdateView.as_view(), name="image_change"
    ),
    path(
        _("element/image/<pk>/delete/"), ImageDeleteView.as_view(), name="image_delete"
    ),
    path(_("element/<pk>/value/add/"), ValueCreateView.as_view(), name="value_create"),
    path(_("element/value/<pk>/"), ValueDetailView.as_view(), name="value_detail"),
    path(
        _("element/value/<pk>/change/"), ValueUpdateView.as_view(), name="value_change"
    ),
    path(
        _("element/value/<pk>/delete/"), ValueDeleteView.as_view(), name="value_delete"
    ),
]
