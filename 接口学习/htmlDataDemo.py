#-*- coding:utf-8 -*-

from html.parser import HTMLParser
import http.client

class BlogHTMLParser(HTMLParser):
    data = []
    data_key = ""

    def __init__(self):
        HTMLParser.__init__(self)
        self.is_a = False
        