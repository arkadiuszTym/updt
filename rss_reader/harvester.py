# -*- coding: utf-8 -*-

"""
author: developed@goodcode.co.uk
date:
licence: Gnu 2.0
description:



"""
import feedparser
from models import News_Item
from django.utils.html import strip_tags
feeds = feedparser.parse('http://www.reddit.com/r/python/.rss')


def harvest():
    for f in feeds['entries']:
        News_Item.objects.create(name=f['title'],
                                 description=strip_tags(f['summary']))
