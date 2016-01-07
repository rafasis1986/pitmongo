# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from pitmongo.utils.functions import generateKey


@python_2_unicode_compatible
class People(models.Model):

    name = models.CharField(_("Name"), max_length=100)
    surname = models.CharField(_("Surname"), max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'
        db_table = 'people_people'

    def save(self, *args, **kwargs):
        self.name = self.name.strip()
        self.surname = self.surname.strip()
        if len(self.slug) == 0:
            self.slug = generateKey()
        super(People, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return "%s, %s" % (self.name, self.surname)

    @models.permalink
    def get_absolute_url(self):
        return ('people:detail', [self.slug])

    @models.permalink
    def get_update_url(self):
        return ('people:update', [self.slug])

    @models.permalink
    def get_delete_url(self):
        return ('people:delete', [self.slug])
