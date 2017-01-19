#/usr/bin/python
# -*- coding: utf-8 -*-

"""
author: developed@goodcode.co.uk
date: Thu 19 Jan 13:06:10 GMT 2017
licence: Gnu 3.0
description:

"""

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime as dt


class Visitor(AbstractUser):
    pass


class News_Item(models.Model):
    """ url name/title and descr of news item """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    source = models.CharField(max_length=20)
    url = models.CharField(max_length=255)
    harvest_date = models.DateField()
    users_fav = models.ManyToManyField(Visitor, null=True, blank=True)

    def __unicode__(self):
        return u"%s: %s" % (self.name, self.url)

    class Meta:
        verbose_name = 'news item'
        verbose_name_plural = 'news items'

    def save(self, force_insert=False, force_update=False, **kwargs):
        self.harvest_date = dt.datetime.now()
        super(News_Item, self).save(force_insert=force_insert,
                                    force_update=force_update)
