from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelChoiceField, ModelForm
from django.utils.translation import gettext_lazy as _
from leaflet.forms.widgets import LeafletWidget
from tinymce.widgets import TinyMCE

from .models import Element, ElementImage, ElementTagValue

User = get_user_model()


class ElementUpdateForm(ModelForm):
    user = ModelChoiceField(
        label=_("Author"), queryset=User.objects.all(), disabled=True
    )

    class Meta:
        model = Element
        fields = ["user", "family", "intro", "geom", "private", "body"]
        widgets = {"geom": LeafletWidget(), "body": TinyMCE()}


class ElementCreateForm(ElementUpdateForm):
    class Media:
        js = ("djeotree/js/locate_user.js",)


class ElementDeleteForm(forms.Form):
    delete = forms.BooleanField(label=_("Check and confirm"), required=True)


class ImageCreateForm(ModelForm):
    class Meta:
        model = ElementImage
        fields = ["image", "description"]


class ValueCreateForm(ModelForm):
    element = ModelChoiceField(
        label=_("Element"), queryset=Element.objects.all(), disabled=True
    )

    class Meta:
        model = ElementTagValue
        fields = ["element", "tag", "value"]
