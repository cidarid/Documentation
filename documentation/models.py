from django.db import models
from django.utils import timezone
from django.urls import reverse
from .snippets import unique_slugify
import os


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('documentation:category', kwargs={'cat_slug': self.slug, 'cat_pk': self.pk})

    def get_edit_url(self):
        return reverse('documentation:edit_category', kwargs={'cat_slug': self.slug, 'cat_pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.name)
        return super().save(*args, **kwargs)


class Documentation(models.Model):
    doc_title = models.CharField(max_length=256)
    slug = models.SlugField(blank=True)
    doc_text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=1)
    date_published = models.DateTimeField('Date published', default=timezone.now)
    date_modified = models.DateTimeField('Date modified', default=timezone.now)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.slug:
            unique_slugify(self, self.doc_title)

    def __str__(self):
        return self.doc_title

    def get_absolute_url(self):
        return reverse('documentation:detail', kwargs={'cat_slug': self.category.slug, 'cat_pk': self.category.pk,
                                                       'doc_slug': self.slug, 'doc_pk': self.pk})

    def get_edit_url(self):
        return reverse('documentation:edit', kwargs={'cat_slug': self.category.slug, 'cat_pk': self.category.pk,
                                                     'doc_slug': self.slug, 'doc_pk': self.pk})

    def get_submit_url(self):
        return reverse('documentation:submit', kwargs={'cat_slug': self.category.slug, 'cat_pk': self.category.pk,
                                                       'doc_slug': self.slug, 'doc_pk': self.pk})


class Document(models.Model):
    doc_file = models.FileField(upload_to='documents/%Y/%m/%d')

    def filename(self):
        return os.path.basename(self.doc_file.name)

# TODO:
# Version history for documentation changes
# No username system needed
# Add categories that the IT team sends over
# Merge main into SpencerBranch
# Add previews in category - e.g.
# --------------------
# |  Category Name   |
# | Category Item #1 |
# | Category Item #2 |
# | etc.             |
# --------------------
# Make the base menu system look better than a bunch of boxes
# Add a download button for documentation
# Allow editing of category names
