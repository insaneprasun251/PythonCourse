import feedparser
import datetime
import delorean
import requests

rss = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
# print(rss.updated)
time_limit = delorean.parse(rss.updated) - datetime.timedelta(hours=6)
entries = [entry for entry in rss.entries if delorean.parse(entry.published) > time_limit]
# print(len(entries))
# print(len(rss.entries))

for entry in entries:
    print(entry['title'], entry['link'])
