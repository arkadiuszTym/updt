RSS reader is test django app used to collect and agregate news.

consists of two major components harvester and rss_reader.

*HARVESTER* 
will collect and process rss feeds from your fav sites
and feed them to your local db.

try
python ../manage.py harvest
to collect latest rss feeds


*READER*
will serve sorted list of news from your sources and allow to search and
display news.  It will provide user accts allowing to save favorites etc.

to migrate new db use:
python ../manage.py migrate --run-syncdb --fake-initial


requirements:
Django version 1.10.5
python 2.7
feedparser (from pip)


I had no time to test with python 3.x but should be easy to port
