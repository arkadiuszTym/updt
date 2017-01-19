#/usr/bin/python
# -*- coding: utf-8 -*-

"""
author: developed@goodcode.co.uk
date: Thu 19 Jan 14:04:29 GMT 2017
licence: Gnu 3.0
description:

"""
from django.test import TestCase

from rss_reader.models import News_Item, Visitor


class RSS_ReaderTestCase(TestCase):
    ''' tests for rss reader '''

    def setUp(self):
        News_Item.objects.create(name="New Django RElesed!",
                                 description='v 4.0.0',
                                 source='http://django-project.com')
        Visitor.objects.create()

    def test_sample_trades(self):
        """add news to visitor's favorite"""
        ni = News_Item.objects.get(name="New Django RElesed!")
        me = Visitor.objects.all()[0]
        ni.users_fav.add(me)
