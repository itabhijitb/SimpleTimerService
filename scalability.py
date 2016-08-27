# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 16:58:26 2016

@author: abhibhat
"""
import requests
import json
one_million = 10**6
status_urls = []
for i in range(one_million):
    if i % 100 == 0:
        print i
    req = requests.post("http://localhost:5000/timer", data={'count': 120})
    status_urls.append(req.headers['Location'])
while any(json.loads(requests.get(status_url))[u'state'] != "SUCCESS"
          for status_url in status_urls):
    pass
print "DONE"
