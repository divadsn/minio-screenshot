#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2

# Shorten URL using Google URL shortener (goo.gl)
def goo_shorten_url(url, api_key):
    postdata = { 'longUrl': url }
    headers = { 'Content-Type': 'application/json' }
    request = urllib2.Request('https://www.googleapis.com/urlshortener/v1/url?key=' + api_key, json.dumps(postdata), headers)

    data = urllib2.urlopen(request).read()
    return json.loads(data)['id']
