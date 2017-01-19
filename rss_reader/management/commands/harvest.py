# -*- coding: utf-8 -*-

"""
author: developed@goodcode.co.uk
date:
licence: Gnu 2.0
description:

"""

from django.core.management.base import BaseCommand, CommandError
from rss_reader.harvester import harvest as hvst

class Command(BaseCommand):
    help = 'harvest known rss feeds'

    def add_arguments(self, parser):
	pass

    def handle(self, *args, **options):
	    try:
		hvst()
            except:
                self.stdout.write(self.style.FAIL('harvest failed.'))
            self.stdout.write(self.style.SUCCESS('harvest compleated.'))

