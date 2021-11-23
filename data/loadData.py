#!/usr/bin/env python
# coding: utf-8

# In[13]:


def generator(dataFrame):
    for line in (dataFrame):
        yield {
            '_index': 'analyzer_artist',
            '_type': '_doc',
            '_id': line.get('No', None),
            '_source': {
                'பெயர்': line.get('பெயர்', None),
                'பாலினம்': line.get('பாலினம்', None),
                'பிறந்த_திகதி': line.get('பிறந்த திகதி', None),
                'பிறந்த_இடம்': line.get('பிறந்த இடம்', None),
                'அறிமுக_படம்': line.get('அறிமுக படம்', None),
                'பணி': line.get('பணி', None),
                'அறிமுகம்': line.get('அறிமுகம்', None),
                'உள்ளடக்கம்': line.get('உள்ளடக்கம்', None)
            }
        }


# In[14]:


try:
    import elasticsearch
    from elasticsearch import Elasticsearch

    import pandas as pd
    import json
    from ast import literal_eval
    from tqdm import tqdm
    import datetime
    import os
    import sys

    import numpy as np
    from elasticsearch import helpers

    print("Modules loaded.......")

except Exception as e:

    print("Some Modules are missing ()".format(e))


# In[17]:


df = pd.read_csv('data.csv')
df.isna().sum()

ENDPOINT = 'http://localhost:9200/'
es = Elasticsearch(timeout=600, hosts=ENDPOINT)

record = df.to_dict('records')
#print(record)


# In[ ]:


#setting for index
#{
#  "settings": {
#    "index": {
#      "number_of_shards": 1,
#      "number_of_replicas": 1
#   },
#   "analysis": {
#      "analyzer": {
#       "my_analyzer": {
#         "tokenizer": "standard",
#         "filter": [ "custom_stop", "custom_stems", "custom_synonyms" ]
#       }
#     },
#     "filter": {
#       "custom_stop": {
#         "type": "stop",
#         "stopwords_path": "analyzer/stopwords.txt"
#       },
#       "custom_stems": {
#        "type": "stemmer_override",
#         "rules_path": "analyzer/stem.txt"
#       },
#       "custom_synonyms": {
#         "type": "synonym",
#         "synonyms_path": "analyzer/synonym.txt"
#       }
#     }
#   }
# },
# "mappings": {
#   "properties": {
#     "பிறந்த_திகதி":{
#       "type": "date"
#     },
#     "அறிமுகம்":{
#       "type": "text"
#     },
#      "உள்ளடக்கம்":{
#       "type": "text"
#      }
#    }
#  }
#}


# In[16]:


mydata = generator(record)

indexName = 'analyzer_artist'
#my = es.indices.create(index=indexName, ignore=[400, 404])

# Uploading documents on elastic search
try:
    res = helpers.bulk(es, mydata)
    print('Uploading...')
except Exception as e:
    print(e)
    pass


# In[ ]:




