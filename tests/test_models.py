from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings

from djeotree.models import Element, Family, Tag, TagValue

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
        c = Family.objects.create(
            user_id=u.uuid,
            title="Child title",
            path="00010001",
            depth=2,
            numchild=0,
        )
        t = Tag.objects.create(user_id=u.uuid, title="Tag title")
        TagValue.objects.create(family_id=f.id, tag_id=t.id, value="Tag value")
        point = '{"type": "Point","coordinates": [12.493652,41.866288]}'
        Element.objects.create(family_id=c.id, intro="foo", location=point)

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
        self.assertEquals(e.get_user(), u)
        print("\n-Tested Element user")

    def test_element_tags(self):
        e = Element.objects.get(intro="foo")
        values = e.element_value.all()
        self.assertEquals(values.count(), 1)
        print("\n-Tested Element tag creation")
