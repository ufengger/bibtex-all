#!/usr/bin/python3

import sys
import requests
import re
import json

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

def get_year(text, bib_dict):
    """Get the year."""
    pattern = '<span class="pl">\s*出版年\s*:</span>.*?(\d{4}).*?<br/>'
    result = re.search(pattern, text)
    if result != None:
        bib_dict['year'] = re.sub('^\s*', '', result.group(1))

def get_pub(text, bib_dict):
    """Get the publisher."""
    pattern = '<span class="pl">\s*出版社\s*:</span>(.*)<br/>'
    result = re.search(pattern, text)
    if result != None:
        bib_dict['publisher'] = re.sub('^\s*', '', result.group(1))

def get_translator(text, bib_dict):
    """Get the translators."""
    pattern = '<span class="pl">\s*译者\s*</span>:(.*?)</span><br/>'
    result = re.search(pattern, text, re.S)
    if result != None:
        text = result.group(1)
        zh = re.findall("[\u4e00-\u9fa5]+", text)
        bib_dict['note'] = ''
        for k in range(len(zh)):
            bib_dict['note'] += zh[k]

def get_extra_title(text, bib_dict):
    """Get the extra title."""
    pattern = '<span class="pl">\s*副标题\s*:</span>(.*?)<br/>'
    result = re.search(pattern, text, re.S)
    if result != None:
        bib_dict['title'] += '：' + re.sub('^\s*', '', result.group(1))

def douban_entry(url, bib_dict):
    """Get a bibtex entry from book.douban.com."""
    r = requests.get(url, headers=headers)
    if r.ok == True:
        get_title_authors(r.text, bib_dict)
        get_year(r.text, bib_dict)
        get_pub(r.text, bib_dict)
        bib_dict['url'] = url
        get_translator(r.text, bib_dict)
        get_extra_title(r.text, bib_dict)
        print(bib_dict)
        return True
    else:
        return False

def bibtex_print(bib_dict, bib_file):
    """Format the bibtex entry, and write it to the bibtex file."""
    entry = '@Book{%s,\n'
    bibtex_key = ''
    if 'author' in bib_dict:
        auth_str = '  author =       {' + bib_dict['author'][0]
        bibtex_key += bib_dict['author'][0]
        for k in range(1, len(bib_dict['author'])):
            auth_str += ' and ' + bib_dict['author'][k]
        auth_str += '},\n'
        entry += auth_str
    if 'title' in bib_dict:
        entry += '  title =        {' + bib_dict['title'] + '},\n'
        idx = bib_dict['title'].find('：')
        if idx == -1:
            bibtex_key += '_' + bib_dict['title']
        else:
            bibtex_key += '_' + bib_dict['title'][:idx]
    if 'year' in bib_dict:
        entry += '  year =         ' + bib_dict['year'] + ',\n'
        bibtex_key += '_' + bib_dict['year']
    if 'publisher' in bib_dict:
        entry += '  publisher =    {' + bib_dict['publisher'] + '},\n'
    if 'url' in bib_dict:
        entry += '  url =          {' + bib_dict['url'] + '},\n'
    if 'note' in bib_dict:
        entry += '  note =         {' + bib_dict['note'] + '译},\n'
    entry += '}\n\n'
    # print(entry %(bibtex_key))
    with open(bib_file, 'a') as f:
        f.write(entry %(bibtex_key))

def bibtex_export(bib_file, url):
    """Export douban url to bibtex entry."""
    bib_dict = {}
    status = douban_entry(url, bib_dict)
    if status:
        bibtex_print(bib_dict, bib_file)
    else:
        print('Something wrong...')

bibtex_export(sys.argv[1], sys.argv[2])
