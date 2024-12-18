import pytest
from django.tests import TestCase
from model_bakery import baker


class FlatPageMetaTagModelTestCase(TestCase):

    def test_save_duplicate_forbidden(self):
        meta_tag = baker.make(
            "flatpage_meta.FlatPageMetaTag", meta_tag_type__allow_multiple=False
        )
        meta_tag.pk = None
        with pytest.raises(ValidationError):
            meta_tag.save()

        meta_tag.meta_tag_type.allow_multiple = True
        meta_tag.meta_tag_type.save()
        meta_tag.save()
