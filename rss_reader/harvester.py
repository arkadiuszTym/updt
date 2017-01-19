# -*- coding: utf-8 -*-

"""
author: developed@goodcode.co.uk
date:
licence: Gnu 3.0
description:

use from ../manage.py harvest command

"""
import feedparser
from models import News_Item
from django.utils.html import strip_tags
feeds = feedparser.parse('http://www.reddit.com/r/python/.rss')


def harvest():
    for f in feeds['entries']:
        News_Item.objects.create(name=f['title'],
                                 description=strip_tags(f['summary']))
