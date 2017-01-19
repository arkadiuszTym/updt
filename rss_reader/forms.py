# -*- coding: utf-8 -*-

"""
author: developed@goodcode.co.uk
date:
licence: Gnu 2.0
description:

"""

from django import forms


class SearchForm(forms.Form):
        query = forms.CharField(label='Search', max_length=100)
