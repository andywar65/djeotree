from django.forms import ModelForm
from leaflet.forms.widgets import LeafletWidget

from .models import Element


class ElementCreateForm(ModelForm):
    class Meta:
        model = Element
        fields = ["user", "family", "intro", "geom"]
        widgets = {"geom": LeafletWidget()}
