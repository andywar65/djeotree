from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings

from djeotree.models import Family, Tag, TagValue

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
            user_id=u.uuid,
            title="Family title",
            path="0001",
            depth=1,
            numchild=1,
        )
        Family.objects.create(
            user_id=u.uuid,
            title="Child title",
            path="00010001",
            depth=2,
            numchild=0,
        )
        t = Tag.objects.create(user_id=u.uuid, title="Tag title")
        TagValue.objects.create(family_id=f.id, tag_id=t.id, value="Tag value")

    def test_model__str__(self):
        f = Family.objects.get(title="Family title")
        self.assertEquals(f.__str__(), "Family title")
        print("\n-Tested Family __str__")
        f = Family.objects.get(title="Child title")
        self.assertEquals(f.__str__(), "-Child title")
        print("\n-Tested child Family __str__")
