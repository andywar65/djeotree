from django.urls import path

from .views import ElementListView

app_name = "geotree"
urlpatterns = [
    path("", ElementListView.as_view(), name="element_list"),
]
