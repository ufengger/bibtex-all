#!/usr/bin/python3

import sys
from os.path import expanduser
from doubanspider import bibtex_export

if len(sys.argv) < 4:
    proxies = {}
else:
    if sys.argv[3] == 'l':
        # lantern proxy
        lantern_conf = expanduser("~") + '/.lantern/settings.yaml'
        with open(lantern_conf, 'r') as file_l:
            contents = file_l.readline()
            addr = contents.split()[1]
            proxies = {
                'http': addr,
                'https': addr,
            }
    elif sys.argv[3] == 'x':
        # v2ray proxy
        addr = '127.0.0.1:8889'
        proxies = {
            'http': addr,
            'https': addr,
        }

bibtex_export(sys.argv[1], sys.argv[2], proxies)
