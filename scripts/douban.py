#!/usr/bin/python3

import sys
import requests
import re
import json
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}

def get_authors(jdict, bib_dict):
    """Get the authors from json dict."""
    num = len(jdict['author'])
    bib_dict['author'] = []
    for k in range(num):
        bib_dict['author'].append(jdict['author'][k]['name'])

def get_title_authors(text, bib_dict):
    """Get the title and author(s)."""
    pattern = '<script type="application/ld\+json">(.*?)</script>'
    ldjson = re.search(pattern, text, re.S)
    if ldjson != None:
        jsondict = json.loads(ldjson.group(1))
        bib_dict['title'] = jsondict['name']
        get_authors(jsondict, bib_dict)

def get_pub(text, bib_dict):
    """Get the publisher."""
    pattern = '<span class="pl">出版社:</span>(.*)<br/>'
    result = re.search(pattern, text)
    if result != None:
        bib_dict['publisher'] = re.sub('^\s*', '', result.group(1))

def douban_entry(url, bib_dict):
    """Get a bibtex entry from book.douban.com."""
    r = requests.get(url, headers=headers)
    if r.ok == True:
        get_pub(r.text, bib_dict)
        get_title_authors(r.text, bib_dict)
        print(bib_dict)
    else:
        print('The url can not be requested.')

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

# bib_dict = {'title': '', 'author': '', 'year': '', 'publisher': '', 'url': '', 'note': ''}
bib_dict = {}

douban_entry(sys.argv[1], bib_dict)
