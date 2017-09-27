#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2

# Shorten URL using Google URL Shortener (goo.gl)
# see https://developers.google.com/url-shortener/v1/getting_started
def goo_shorten_url(url, api_key):
    api_url = "https://www.googleapis.com/urlshortener/v1/url?key=%s"
    request = urllib2.Request(api_url % api_key, json.dumps({ "longUrl": url }), { 'Content-Type': 'application/json' })
    data = urllib2.urlopen(request).read()
    return json.loads(data)['id']
