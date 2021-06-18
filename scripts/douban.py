#!/usr/bin/python3

import sys
from doubanspider import bibtex_export
if len(sys.argv) < 4:
    proxies = {}
else:
    proxies = {
        'http': '127.0.0.1:37013',
        'https': '127.0.0.1:37013',
    }

bibtex_export(sys.argv[1], sys.argv[2], proxies)
