#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

with open("../problem/characters.html","rb") as html_page:
    for line in html_page:
        match = re.search('href="/wiki/([\w\_]+)"\s+title="([\w\s]+)"',line)
        if match:
            print "Url: ", match.group(1), "\nName: ", match.group(2)
