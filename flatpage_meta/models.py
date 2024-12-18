from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.db import models


class MetaTagType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    format_string = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True, null=True)
    allow_multiple = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CommonMetaTag(models.Model):
    meta_tag_type = models.ForeignKey(
        MetaTagType,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
    )
    content = models.TextField(max_length=350)

    class Meta:
        verbose_name = "Meta tag"
        abstract = True

    def __str__(self):
        return self.meta_tag_type.format_string.format(content=self.content)


class FlatPageMetaTag(CommonMetaTag):
    flatpage = models.ForeignKey(
        FlatPage, on_delete=models.CASCADE, related_name="meta_tag_set"
    )

    def clean(self):
        if not self.meta_tag_type.allow_multiple and self.flatpage.pk:
            if FlatPageMetaTag.objects.filter(
                flatpage=self.flatpage, meta_tag_type=self.meta_tag_type
            ).exclude(pk=self.pk):
                raise ValidationError(
                    "You can only have one {tag} tag per FlatPage".format(
                        tag=self.meta_tag_type
                    )
                )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class SiteMetaTag(CommonMetaTag):
    site = models.ForeignKey(
        Site, on_delete=models.CASCADE, related_name="meta_tag_set"
    )

    def clean(self):
        if not self.meta_tag_type.allow_multiple:
            if SiteMetaTag.objects.filter(
                site=self.site, meta_tag_type=self.meta_tag_type
            ).exclude(pk=self.pk):
                raise ValidationError(
                    "You can only have one {tag} tag per Site".format(
                        tag=self.meta_tag_type
                    )
                )
