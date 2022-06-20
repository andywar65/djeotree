from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from djgeojson.fields import MultiLineStringField, PointField
from filebrowser.base import FileObject
from filebrowser.fields import FileBrowseField
from treebeard.mp_tree import MP_Node

User = get_user_model()


class Tag(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_tag",
        verbose_name=_("Author"),
    )
    title = models.CharField(
        _("Title"),
        help_text=_("Tag name"),
        max_length=50,
    )

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        ordering = ("user", "title")

    def __str__(self):
        return self.title


class Family(MP_Node):
    node_order_by = ["title"]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_family",
        verbose_name=_("Author"),
    )
    title = models.CharField(
        _("Title"),
        help_text=_("Family name"),
        max_length=50,
    )
    intro = models.CharField(
        _("Description"),
        null=True,
        blank=True,
        help_text=_("Few words to describe the family"),
        max_length=100,
    )
    geom = MultiLineStringField(null=True)

    class Meta:
        verbose_name = _("Element Family")
        verbose_name_plural = _("Element Families")

    def __str__(self):
        prefix = ""
        for i in range(self.depth - 1):
            prefix = prefix + "-"
        return prefix + self.title

    def save(self, *args, **kwargs):
        coords = []
        elements = self.family_element.all().order_by("date")
        for e in elements:
            coords.append(e.geom["coordinates"])
        self.geom = {"type": "MultiLineString", "coordinates": [coords]}
        super(Family, self).save(*args, **kwargs)


class TagValue(models.Model):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="tag_value",
        verbose_name=_("Tag"),
    )
    family = models.ForeignKey(
        Family,
        on_delete=models.CASCADE,
        related_name="family_value",
        verbose_name=_("Family"),
    )
    value = models.CharField(
        _("Value"),
        help_text=_("Tag value"),
        max_length=200,
    )

    class Meta:
        verbose_name = _("Tag value")
        verbose_name_plural = _("Tag values")


class Element(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_element",
        verbose_name=_("Author"),
    )
    family = models.ForeignKey(
        Family,
        on_delete=models.CASCADE,
        related_name="family_element",
        verbose_name=_("Family"),
    )
    intro = models.CharField(_("Description"), null=True, max_length=200)
    body = models.TextField(_("Text"), null=True, blank=True)
    date = models.DateTimeField(
        _("Date"),
        default=now,
    )
    geom = PointField()
    private = models.BooleanField(_("Private element"), default=False)

    class Meta:
        verbose_name = _("Element")
        verbose_name_plural = _("Elements")

    @property
    def popupContent(self):
        url = reverse(
            "geotree:element_detail",
            kwargs={"username": self.user.username, "pk": self.id},
        )
        title_str = '<h5><a href="%(url)s">%(title)s</a></h5>' % {
            "title": self.__str__(),
            "url": url,
        }
        intro_str = "<small>%(intro)s</small>" % {"intro": self.intro}
        image = self.get_first_image()
        if not image:
            return title_str + intro_str
        image_str = '<img src="%(image)s">' % {"image": image}
        return title_str + image_str + intro_str

    def __str__(self):
        return self.family.title + "-" + str(self.id)

    def get_user(self):
        return self.family.user

    def get_first_image(self):
        image = self.element_image.first()
        if not image:
            return
        path = image.fb_image.version_generate("popup").path
        return settings.MEDIA_URL + path

    get_user.short_description = _("Author")


class ElementTagValue(models.Model):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="element_tag_value",
        verbose_name=_("Tag"),
    )
    element = models.ForeignKey(
        Element,
        on_delete=models.CASCADE,
        related_name="element_value",
        verbose_name=_("Element"),
    )
    value = models.CharField(
        _("Value"),
        help_text=_("Tag value"),
        max_length=200,
    )

    class Meta:
        verbose_name = _("Tag value")
        verbose_name_plural = _("Tag values")


class ElementImage(models.Model):
    element = models.ForeignKey(
        Element,
        on_delete=models.CASCADE,
        related_name="element_image",
        verbose_name=_("Article"),
    )
    description = models.CharField(
        _("Description"),
        help_text=_("Used in captions"),
        max_length=200,
        null=True,
        blank=True,
    )
    fb_image = FileBrowseField(
        _("Image"),
        max_length=200,
        extensions=[".jpg", ".png", ".jpeg", ".gif", ".tif", ".tiff"],
        directory="images/element/",
        null=True,
    )
    image = models.ImageField(
        _("Image"),
        max_length=200,
        null=True,
        upload_to="uploads/images/element/",
    )
    position = models.PositiveSmallIntegerField(_("Position"), null=True)

    class Meta:
        verbose_name = _("Element image")
        verbose_name_plural = _("Element images")
        ordering = [
            "position",
        ]

    def save(self, *args, **kwargs):
        # save and upload image
        super(ElementImage, self).save(*args, **kwargs)
        if self.image:
            # image is saved on the front end, passed to fb_image and deleted
            self.fb_image = FileObject(str(self.image))
            # check_tall_image(self.fb_image)
            self.image = None
            super(ElementImage, self).save(*args, **kwargs)
