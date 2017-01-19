# -*- coding: utf-8 -*-

"""
author: developed@goodcode.co.uk
date:
licence: Gnu 2.0
description:

"""

from rss_reader.models import News_Item
from django.views.generic import TemplateView
from forms import SearchForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


class Render_FrontPage(TemplateView):
    template_name = 'news_list.html'

    def dispatch(self, *args, **kwargs):
        return super(Render_FrontPage, self).dispatch(*args, **kwargs)

    def get_context_data(self,  **kwargs):
        ctx = {
            'news': News_Item.objects.order_by('harvest_date'),
        }
        return ctx

# quick and dirty search ( I got no time left )
def SearchPage(request):
    query = request.POST['search']
    results = News_Item.objects.filter(
            description__contains=query)

    return render(request, 'search.html', 
                  { 'results': results })

