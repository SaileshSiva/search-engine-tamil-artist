# -*- coding: utf-8 -*-
"""Scraper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-PZySPOJZ15LTi04n5osuaSz1kbTPw8z
"""

import csv

import requests
from bs4 import BeautifulSoup

csv_columns = ['No','பெயர்', 'பாலினம்','பிறந்த திகதி', 'பிறந்த இடம்', 'அறிமுக படம்', 'பணி', 'அறிமுகம்', 'உள்ளடக்கம்']

actress_links = ['https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%95%E0%AF%8D%E0%AE%9A%E0%AE%B0%E0%AE%BE_%E0%AE%B9%E0%AE%BE%E0%AE%9A%E0%AE%A9%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%95%E0%AE%BE%E0%AE%A9%E0%AE%BE',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%9E%E0%AF%8D%E0%AE%9A%E0%AE%B2%E0%AE%BF_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AF%88)',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%A4%E0%AE%BF%E0%AE%A4%E0%AE%BF_%E0%AE%AA%E0%AE%BE%E0%AE%B2%E0%AE%A9%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%A4%E0%AE%BF%E0%AE%A4%E0%AE%BF_%E0%AE%B0%E0%AE%BE%E0%AE%B5%E0%AF%8D_%E0%AE%B9%E0%AF%88%E0%AE%A4%E0%AE%BE%E0%AE%B0%E0%AE%BF',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%AE%E0%AF%8D%E0%AE%AA%E0%AE%BF%E0%AE%95%E0%AE%BE_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AF%88)',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%B0%E0%AF%81%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%A4%E0%AE%BF_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AF%88)',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AE%95%E0%AF%80%E0%AE%B2%E0%AE%BE',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%95%E0%AF%80%E0%AE%B0%E0%AF%8D%E0%AE%A4%E0%AF%8D%E0%AE%A4%E0%AE%BF_%E0%AE%9A%E0%AF%81%E0%AE%B0%E0%AF%87%E0%AE%B7%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%95%E0%AF%81%E0%AE%B7%E0%AF%8D%E0%AE%AA%E0%AF%82',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%95%E0%AE%BE%E0%AE%B0%E0%AF%8D%E0%AE%A4%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%95%E0%AE%BE_%E0%AE%A8%E0%AE%BE%E0%AE%AF%E0%AE%B0%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%95%E0%AE%B8%E0%AF%8D%E0%AE%A4%E0%AF%82%E0%AE%B0%E0%AE%BF_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AF%88)',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%95%E0%AE%AE%E0%AE%B2%E0%AE%BF%E0%AE%A9%E0%AE%BF_%E0%AE%AE%E0%AF%81%E0%AE%95%E0%AE%B0%E0%AF%8D%E0%AE%9C%E0%AE%BF',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%AE%E0%AE%B2%E0%AE%BE_%E0%AE%AA%E0%AE%BE%E0%AE%B2%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%AA%E0%AE%BF%E0%AE%B0%E0%AE%BE%E0%AE%AE%E0%AE%BF_%E0%AE%9A%E0%AF%81%E0%AE%B0%E0%AF%87%E0%AE%B7%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%90%E0%AE%B8%E0%AF%8D%E0%AE%B5%E0%AE%B0%E0%AF%8D%E0%AE%AF%E0%AE%BE_%E0%AE%B0%E0%AE%BE%E0%AE%AF%E0%AF%8D_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AF%88)',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%90%E0%AE%B8%E0%AF%8D%E0%AE%B5%E0%AE%B0%E0%AF%8D%E0%AE%AF%E0%AE%BE_%E0%AE%87%E0%AE%B2%E0%AE%9F%E0%AF%8D%E0%AE%9A%E0%AF%81%E0%AE%AE%E0%AE%BF',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%90%E0%AE%B8%E0%AF%8D%E0%AE%B5%E0%AE%B0%E0%AF%8D%E0%AE%AF%E0%AE%BE_%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AF%87%E0%AE%B7%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%8E%E0%AE%B2%E0%AF%8D._%E0%AE%B5%E0%AE%BF%E0%AE%9C%E0%AE%AF%E0%AE%B2%E0%AE%9F%E0%AF%8D%E0%AE%9A%E0%AF%81%E0%AE%AE%E0%AE%BF',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%95%E0%AE%9C%E0%AF%8B%E0%AE%B2%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%A9%E0%AF%81_%E0%AE%B9%E0%AE%BE%E0%AE%9A%E0%AE%A9%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%95%E0%AF%87._%E0%AE%86%E0%AE%B0%E0%AF%8D._%E0%AE%B5%E0%AE%BF%E0%AE%9C%E0%AE%AF%E0%AE%BE',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BE%E0%AE%AF%E0%AF%8D_%E0%AE%AA%E0%AE%B2%E0%AF%8D%E0%AE%B2%E0%AE%B5%E0%AE%BF',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BE%E0%AE%B2%E0%AE%BF%E0%AE%A9%E0%AE%BF_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AF%88)',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%AE%E0%AF%8D%E0%AE%B0%E0%AE%A9%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AF%81%E0%AE%B0%E0%AF%81%E0%AE%A4%E0%AE%BF_%E0%AE%B9%E0%AE%BE%E0%AE%9A%E0%AE%A9%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%A8%E0%AE%BF%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%BF_%E0%AE%95%E0%AE%B2%E0%AF%8D%E0%AE%B0%E0%AE%BE%E0%AE%A9%E0%AE%BF',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%A8%E0%AE%AF%E0%AE%A9%E0%AF%8D%E0%AE%A4%E0%AE%BE%E0%AE%B0%E0%AE%BE',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%A8%E0%AE%95%E0%AF%8D%E0%AE%AE%E0%AE%BE',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%A8%E0%AE%BF%E0%AE%B5%E0%AF%87%E0%AE%A4%E0%AE%BE_%E0%AE%A4%E0%AE%BE%E0%AE%AE%E0%AE%B8%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%A4%E0%AF%8D%E0%AE%AE%E0%AE%BF%E0%AE%A9%E0%AE%BF',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%BE%E0%AE%A9%E0%AF%81%E0%AE%AA%E0%AF%8D%E0%AE%B0%E0%AE%BF%E0%AE%AF%E0%AE%BE_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AF%88)',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%AE%E0%AF%87%E0%AE%95%E0%AE%BE_%E0%AE%86%E0%AE%95%E0%AE%BE%E0%AE%B7%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%BE%E0%AE%B0%E0%AF%8D%E0%AE%B5%E0%AE%A4%E0%AE%BF_%E0%AE%93%E0%AE%AE%E0%AE%A9%E0%AE%95%E0%AF%81%E0%AE%9F%E0%AF%8D%E0%AE%9F%E0%AE%A9%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%BE%E0%AE%B5%E0%AE%A9%E0%AE%BE',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%BF%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AF%81_%E0%AE%AE%E0%AE%BE%E0%AE%A4%E0%AE%B5%E0%AE%BF',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%BF%E0%AE%B0%E0%AE%BF%E0%AE%AF%E0%AE%BE_%E0%AE%86%E0%AE%A9%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AF%81',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%B0%E0%AE%BE%E0%AE%A3%E0%AE%BF_%E0%AE%AE%E0%AF%81%E0%AE%95%E0%AE%B0%E0%AF%8D%E0%AE%9C%E0%AE%BF',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%AE%E0%AE%95%E0%AE%BF%E0%AE%AE%E0%AE%BE_%E0%AE%A8%E0%AE%AE%E0%AF%8D%E0%AE%AA%E0%AE%BF%E0%AE%AF%E0%AE%BE%E0%AE%B0%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%9C%E0%AF%86%E0%AE%A9%E0%AE%BF%E0%AE%B2%E0%AE%BF%E0%AE%AF%E0%AE%BE',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%9C%E0%AF%86._%E0%AE%9C%E0%AF%86%E0%AE%AF%E0%AE%B2%E0%AE%B2%E0%AE%BF%E0%AE%A4%E0%AE%BE',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%B0%E0%AE%AE%E0%AF%8D%E0%AE%AF%E0%AE%BE_%E0%AE%A8%E0%AE%AE%E0%AF%8D%E0%AE%AA%E0%AF%80%E0%AE%9A%E0%AE%A9%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%BE%E0%AE%B0%E0%AF%8D%E0%AE%B5%E0%AE%A4%E0%AE%BF_%E0%AE%AE%E0%AF%87%E0%AE%A9%E0%AE%A9%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%B5%E0%AE%BF%E0%AE%9C%E0%AE%AF%E0%AE%9A%E0%AE%BE%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%BF',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%B5%E0%AF%88%E0%AE%AA%E0%AE%B5%E0%AE%BF_%E0%AE%9A%E0%AE%BE%E0%AE%A3%E0%AF%8D%E0%AE%9F%E0%AE%BF%E0%AE%B2%E0%AF%8D%E0%AE%AF%E0%AE%BE',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%B2%E0%AE%BE%E0%AE%B8%E0%AF%8D%E0%AE%B2%E0%AE%BF%E0%AE%AF%E0%AE%BE_%E0%AE%AE%E0%AE%B0%E0%AE%BF%E0%AE%AF%E0%AE%A9%E0%AF%87%E0%AE%9A%E0%AE%A9%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%B2%E0%AE%9F%E0%AF%8D%E0%AE%9A%E0%AF%81%E0%AE%AE%E0%AE%BF_%E0%AE%AE%E0%AF%87%E0%AE%A9%E0%AE%A9%E0%AF%8D_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AF%88)',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%AE%E0%AE%AE%E0%AF%8D%E0%AE%A4%E0%AE%BE_%E0%AE%AE%E0%AF%8B%E0%AE%95%E0%AE%A9%E0%AF%8D%E0%AE%A4%E0%AE%BE%E0%AE%B8%E0%AF%8D',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%AE%E0%AE%A4%E0%AF%81_%E0%AE%9A%E0%AE%BE%E0%AE%B2%E0%AE%BF%E0%AE%A9%E0%AE%BF',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AF%82%E0%AE%9C%E0%AE%BE_%E0%AE%B9%E0%AF%86%E0%AE%95%E0%AF%8D%E0%AE%9F%E0%AF%87',
                 'https://ta.m.wikipedia.org/wiki/%E0%AE%AE%E0%AE%A9%E0%AF%8B%E0%AE%B0%E0%AE%AE%E0%AE%BE_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AF%88)']

actor_links = ['https://ta.m.wikipedia.org/wiki/%E0%AE%B5%E0%AE%BF%E0%AE%A9%E0%AE%AF%E0%AF%8D', 
               'https://ta.m.wikipedia.org/wiki/%E0%AE%95%E0%AE%BE%E0%AE%B0%E0%AF%8D%E0%AE%A4%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%95%E0%AF%8D_%E0%AE%9A%E0%AE%BF%E0%AE%B5%E0%AE%95%E0%AF%81%E0%AE%AE%E0%AE%BE%E0%AE%B0%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%BF%E0%AE%B0%E0%AE%BF%E0%AE%A4%E0%AF%8D%E0%AE%B5%E0%AE%BF%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AF%8D_%E0%AE%9A%E0%AF%81%E0%AE%95%E0%AF%81%E0%AE%AE%E0%AE%BE%E0%AE%B0%E0%AE%A9%E0%AF%8D', 
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9C%E0%AF%80%E0%AE%B5%E0%AE%BE_(%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AF%88%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AE%9F_%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AE%B0%E0%AF%8D)', 
               'https://ta.m.wikipedia.org/wiki/%E0%AE%B5%E0%AE%BF%E0%AE%B7%E0%AE%BE%E0%AE%B2%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%B0%E0%AE%A4%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%86%E0%AE%B0%E0%AF%8D%E0%AE%AF%E0%AE%BE',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9C%E0%AF%86%E0%AE%AF%E0%AE%AE%E0%AF%8D_%E0%AE%B0%E0%AE%B5%E0%AE%BF',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%A4%E0%AE%A9%E0%AF%81%E0%AE%B7%E0%AF%8D_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AE%B0%E0%AF%8D)',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%B8%E0%AF%8D%E0%AE%B0%E0%AF%80%E0%AE%95%E0%AE%BE%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AF%8D_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AE%B0%E0%AF%8D)', 
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BE%E0%AE%AE%E0%AF%8D_(%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4%E0%AF%8D_%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AE%B0%E0%AF%8D)',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%B2%E0%AE%AE%E0%AF%8D%E0%AE%AA%E0%AE%B0%E0%AE%9A%E0%AE%A9%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%AE%E0%AE%BE%E0%AE%A4%E0%AE%B5%E0%AE%A9%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AF%82%E0%AE%B0%E0%AF%8D%E0%AE%AF%E0%AE%BE_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AE%B0%E0%AF%8D)',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%9C%E0%AE%BF%E0%AE%A4%E0%AF%8D_%E0%AE%95%E0%AF%81%E0%AE%AE%E0%AE%BE%E0%AE%B0%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%B5%E0%AE%BF%E0%AE%9C%E0%AE%AF%E0%AF%8D_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AE%B0%E0%AF%8D)',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AE%BE%E0%AE%B8%E0%AF%8D_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AE%B0%E0%AF%8D)',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%BF%E0%AE%B0%E0%AE%9A%E0%AE%BE%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%BF%E0%AE%B0%E0%AE%AA%E0%AF%81%E0%AE%A4%E0%AF%87%E0%AE%B5%E0%AE%BE',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%B5%E0%AE%BF%E0%AE%95%E0%AF%8D%E0%AE%B0%E0%AE%AE%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%B5%E0%AE%BF%E0%AE%B5%E0%AF%87%E0%AE%95%E0%AF%8D_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AE%B0%E0%AF%8D)',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%A4%E0%AF%81%E0%AE%B0%E0%AF%88%E0%AE%9A%E0%AE%BE%E0%AE%AE%E0%AE%BF_%E0%AE%A8%E0%AF%86%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AF%8B%E0%AE%B2%E0%AE%BF%E0%AE%AF%E0%AE%A9%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%B5%E0%AE%9F%E0%AE%BF%E0%AE%B5%E0%AF%87%E0%AE%B2%E0%AF%81_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AE%B0%E0%AF%8D)',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BE%E0%AE%B0%E0%AF%8D%E0%AE%B2%E0%AE%BF',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AE%B0%E0%AE%A4%E0%AF%8D%E0%AE%95%E0%AF%81%E0%AE%AE%E0%AE%BE%E0%AE%B0%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AF%86%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%B2%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%95%E0%AE%B5%E0%AF%81%E0%AE%A3%E0%AF%8D%E0%AE%9F%E0%AE%AE%E0%AE%A3%E0%AE%BF',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%B5%E0%AE%BF%E0%AE%9C%E0%AE%AF%E0%AE%95%E0%AF%81%E0%AE%AE%E0%AE%BE%E0%AE%B0%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AE%A4%E0%AF%8D%E0%AE%AF%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%BE%E0%AE%B0%E0%AF%8D%E0%AE%A4%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%AA%E0%AE%A9%E0%AF%8D_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AE%B0%E0%AF%8D)',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AE%A9%E0%AE%95%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%B0%E0%AF%8D%E0%AE%9C%E0%AF%81%E0%AE%A9%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%B5%E0%AE%BF%E0%AE%9A%E0%AE%AF%E0%AE%95%E0%AE%BE%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AF%81',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%B5%E0%AE%BF%E0%AE%9A%E0%AE%AF%E0%AE%95%E0%AE%BE%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AF%81',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%BE%E0%AE%95%E0%AF%8D%E0%AE%AF%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%AA%E0%AE%BE%E0%AE%A3%E0%AF%8D%E0%AE%9F%E0%AE%BF%E0%AE%AF%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AE%A9%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%95%E0%AE%AE%E0%AE%B2%E0%AF%8D%E0%AE%B9%E0%AE%BE%E0%AE%9A%E0%AE%A9%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%87%E0%AE%B0%E0%AE%9A%E0%AE%BF%E0%AE%A9%E0%AE%BF%E0%AE%95%E0%AE%BE%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AF%81',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AF%81%E0%AE%B0%E0%AF%81%E0%AE%B3%E0%AE%BF_%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AE%A9%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%A4%E0%AF%87%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%BE%E0%AE%AF%E0%AF%8D_%E0%AE%9A%E0%AF%80%E0%AE%A9%E0%AE%BF%E0%AE%B5%E0%AE%BE%E0%AE%9A%E0%AE%A9%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%A8%E0%AE%BE%E0%AE%95%E0%AF%87%E0%AE%B7%E0%AF%8D', 
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%B5%E0%AE%BE%E0%AE%9C%E0%AE%BF_%E0%AE%95%E0%AE%A3%E0%AF%87%E0%AE%9A%E0%AE%A9%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%AE._%E0%AE%95%E0%AF%8B._%E0%AE%87%E0%AE%B0%E0%AE%BE%E0%AE%AE%E0%AE%9A%E0%AF%8D%E0%AE%9A%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AE%A9%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9C%E0%AF%86%E0%AE%AE%E0%AE%BF%E0%AE%A9%E0%AE%BF_%E0%AE%95%E0%AE%A3%E0%AF%87%E0%AE%9A%E0%AE%A9%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%B5%E0%AE%BF._%E0%AE%95%E0%AF%87._%E0%AE%B0%E0%AE%BE%E0%AE%AE%E0%AE%9A%E0%AE%BE%E0%AE%AE%E0%AE%BF',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%8E%E0%AE%AE%E0%AF%8D._%E0%AE%86%E0%AE%B0%E0%AF%8D._%E0%AE%B0%E0%AE%BE%E0%AE%A4%E0%AE%BE',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%AE%E0%AE%BE._%E0%AE%A8%E0%AE%BE._%E0%AE%A8%E0%AE%AE%E0%AF%8D%E0%AE%AA%E0%AE%BF%E0%AE%AF%E0%AE%BE%E0%AE%B0%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9C%E0%AF%86%E0%AE%AF%E0%AF%8D%E0%AE%9A%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%B0%E0%AF%8D',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%B0%E0%AE%B5%E0%AE%BF%E0%AE%9A%E0%AF%8D%E0%AE%9A%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AE%A9%E0%AF%8D_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AE%B0%E0%AF%8D)',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%9C%E0%AF%87._%E0%AE%AA%E0%AE%BF._%E0%AE%9A%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AE%AA%E0%AE%BE%E0%AE%AA%E0%AF%81',
               'https://ta.m.wikipedia.org/wiki/%E0%AE%AE%E0%AF%87%E0%AE%9C%E0%AE%B0%E0%AF%8D_%E0%AE%9A%E0%AF%81%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%B0%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AE%A9%E0%AF%8D']

def get_paragraph(soup_new):
    para1 = None
    para2 = None

    try:
        parser_contents = soup_new.find('section', {"class":"mf-section-0"}).contents
        for i in parser_contents:
            if i.name == 'p':
                if para1 == None:
                    para1 = i.text.strip()
                    continue
                if para2 == None:
                    para2 = i.text.strip()
                    break
        return (para1, para2)
    except AttributeError:
        return (para1, para2)

def getBirthDetails(soup_new):
    birthdate = None
    birthplace = None
    try:
        info_box = soup_new.find('table', {'class': 'infobox'})
        table_row_list = info_box.findAll('tr')
    except TypeError or AttributeError:
        return (birthdate, birthplace)

    for tr in table_row_list:
        try:
            if ((tr.th.text).strip() == 'பிறப்பு'):
                if tr.td.findAll('span', {'class': 'bday'}):
                    birthdate = tr.td.find('span', {'class': 'bday'}).text
                if tr.td.findAll('span', {'class': 'birthplace'}):
                    birthplace = tr.td.find('span', {'class': 'birthplace'}).text
                else:
                    try:
                        string_br = str(tr.td)
                        if '<br/>' in string_br:
                            splitted_with_break = string_br.split('<br/>')
                            birthplace = (BeautifulSoup(splitted_with_break[-1], "html.parser").text.strip())
                            if birthplace == '':
                                birthplace = None
                    except AttributeError:
                        continue
        except AttributeError or TypeError:
            continue
    return (birthdate, birthplace)

def name(soup_new):
  actor_name = soup_new.find('h1').text
  final_name = actor_name.split("(")
  return final_name[0]

def occupation(soup_new):
  occu = 'திரைப்பட நடிகர்'
  try:
    info_box = soup_new.find('table',{'class':'infobox'})
    table_row_list = info_box.findAll('tr')
  except TypeError or AttributeError :
    return(occu)
  for i in table_row_list:
    try:
      if ((i.th.text).strip() == 'தொழில்' or (i.th.text).strip() == 'பணி'):
        occu = i.td.text
        return (occu)
    except AttributeError or TypeError:
      continue
  return occu

vijay_link = 'https://ta.m.wikipedia.org/wiki/%E0%AE%85%E0%AE%95%E0%AF%8D%E0%AE%9A%E0%AE%B0%E0%AE%BE_%E0%AE%B9%E0%AE%BE%E0%AE%9A%E0%AE%A9%E0%AF%8D'
get_url = requests.get(vijay_link)
get_text = get_url.text
soup_new = BeautifulSoup(get_text, "html.parser")

get_paragraph(soup_new)

dict_data= []
count = 1
person_lists = actor_links + actress_links
for i in range(len(person_lists)):
  dict = {}
  hurl = person_lists[i]
  response_new = requests.get(hurl)
  response_text = response_new.text
  soup_new = BeautifulSoup(response_text, "html.parser")
  try:
    bday,birthplace = getBirthDetails(soup_new)
    para1,para2 = get_paragraph(soup_new)
    actor_name = name(soup_new)
    occ = occupation(soup_new)

    debFilm = input("Enter the debut film for " + actor_name + ":")

  except AttributeError or TypeError:
    #print("Error found")
    bday = 'தகவல் இல்லை'
    birthplace = 'இந்தியா'
    actor_name = 'XXXX'
    occ = 'திரைப்பட நடிகர்'

  if hurl in actor_links:
    dict[csv_columns[2]] = 'ஆண்'
  else:
    dict[csv_columns[2]] = 'பெண்'

  dict[csv_columns[1]] = actor_name
  dict[csv_columns[6]] = occ
  dict[csv_columns[7]] = para1
  dict[csv_columns[0]] = count
  dict[csv_columns[3]] = bday
  dict[csv_columns[4]] = birthplace
  dict[csv_columns[5]] = debFilm
  dict[csv_columns[8]] = para2



  dict_data.append(dict)
  count +=1


csv_file = 'data.csv'

try:
    with open(csv_file,'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)

except IOError:
    print("I/O error")

import pandas as pd

path = '/content/data.csv'

output_scrap = pd.read_csv(path)

output_scrap.T