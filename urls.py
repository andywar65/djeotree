from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import (
    AuthorDetailView,
    AuthorListView,
    BaseListView,
    ElementDayArchiveView,
    ElementDetailView,
    ElementMonthArchiveView,
    ElementYearArchiveView,
    FamilyDetailView,
    FamilyListView,
    TagDetailView,
    TagListView,
)

app_name = "geotree"
urlpatterns = [
    path("", BaseListView.as_view(), name="base_list"),
    path(_("families"), FamilyListView.as_view(), name="family_list"),
    path(_("authors"), AuthorListView.as_view(), name="author_list"),
    path(_("tags"), TagListView.as_view(), name="tag_list"),
    path(_("family/<pk>"), FamilyDetailView.as_view(), name="family_detail"),
    path(_("author/<username>"), AuthorDetailView.as_view(), name="author_detail"),
    path(_("tag/<pk>"), TagDetailView.as_view(), name="tag_detail"),
    path(
        _("author/<username>/element/<pk>"),
        ElementDetailView.as_view(),
        name="element_detail",
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
]
