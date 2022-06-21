from django.contrib.auth import get_user_model
from django.forms import ModelChoiceField, ModelForm
from django.utils.translation import gettext_lazy as _
from leaflet.forms.widgets import LeafletWidget

from .models import Element

User = get_user_model()


class ElementCreateForm(ModelForm):
    user = ModelChoiceField(
        label=_("Author"), queryset=User.objects.all(), disabled=True
    )

    class Meta:
        model = Element
        fields = ["user", "family", "intro", "geom", "private"]
        widgets = {"geom": LeafletWidget()}
