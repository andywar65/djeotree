from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings

from djeotree.models import Element, ElementImage, Family, Tag, TagValue

User = get_user_model()


@override_settings(USE_I18N=False)
class DjeotreeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("\nTest djeotree models")
        # Set up non-modified objects used by all test methods
        u = User.objects.create(
            username="andy.war65",
            password="P4s5W0r6",
            email="andy@war.com",
        )
        f = Family.objects.create(
            title="Family title",
            path="0001",
            depth=1,
            numchild=1,
        )
        c = Family.objects.create(
            title="Child title",
            path="00010001",
            depth=2,
            numchild=0,
        )
        t = Tag.objects.create(title="Tag title")
        TagValue.objects.create(family_id=f.id, tag_id=t.id, value="Tag value")
        point = '{"type": "Point","coordinates": [12.493652,41.866288]}'
        Element.objects.create(user_id=u.uuid, family_id=c.id, intro="foo", geom=point)

    def test_model__str__(self):
        f = Family.objects.get(title="Family title")
        self.assertEquals(f.__str__(), "Family title")
        print("\n-Tested Family __str__")
        c = Family.objects.get(title="Child title")
        self.assertEquals(c.__str__(), "-Child title")
        print("\n-Tested child Family __str__")
        t = Tag.objects.get(title="Tag title")
        self.assertEquals(t.__str__(), "Tag title")
        print("\n-Tested Tag __str__")
        e = Element.objects.get(intro="foo")
        self.assertEquals(e.__str__(), "Child title-" + str(e.id))
        print("\n-Tested Element __str__")

    def test_element_user(self):
        u = User.objects.get(username="andy.war65")
        e = Element.objects.get(intro="foo")
        self.assertEquals(e.user, u)
        print("\n-Tested Element user")

    def test_element_tags(self):
        e = Element.objects.get(intro="foo")
        values = e.element_value.all()
        self.assertEquals(values.count(), 1)
        print("\n-Tested Element tag creation")


@override_settings(MEDIA_ROOT=Path(settings.MEDIA_ROOT).joinpath("temp"))
class ElementImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("\nTest element image model")
        # Set up non-modified objects used by all test methods
        u = User.objects.create(
            username="raw.ydna56", password="P4s5W0r6", email="ydna@raw.com"
        )
        f = Family.objects.create(
            title="Family title",
            path="0002",
            depth=1,
            numchild=0,
        )
        point = '{"type": "Point","coordinates": [12.493652,41.866288]}'
        e = Element.objects.create(
            user_id=u.uuid, family_id=f.id, intro="bar", geom=point
        )
        img = ElementImage(element_id=e.id, description="taz")
        img_path = Path(settings.STATIC_ROOT).joinpath("tests/image.jpg")
        with open(img_path, "rb") as file:
            content = file.read()
        img.image = SimpleUploadedFile("image.jpg", content, "image/jpg")
        img.save()

    def tearDown(self):
        """Checks existing files, then removes them"""
        path = Path(settings.MEDIA_ROOT).joinpath("uploads/images/element/")
        list = [e for e in path.iterdir() if e.is_file()]
        for file in list:
            Path(file).unlink()

    def test_element_fb_image(self):
        img = ElementImage.objects.get(description="taz")
        self.assertEquals(img.image, "")
        print("\n-Tested Element Image image")
        self.assertEquals(img.fb_image.path, "uploads/images/element/image.jpg")
        print("\n-Tested Element Image fb_image")
