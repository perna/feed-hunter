# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import re
import json

class FeedEaterPipeline(object):

    def process_item(self, item, spider):

        data = {
            'name': item['name'],
            'feed': self.get_feed(self.get_id(item['url']))
        }
        
        header = {'Content-type': 'application/json'}
        req = requests.post('https://podigger.xyz/api/podcasts/', data=json.dumps(data), headers=header)
        return item


    def get_id(self, url):
        id_podcast = re.search('id(\d+)', url).groups()[0]
        return id_podcast


    def get_feed(self, id_podcast):
        req = requests.get('https://itunes.apple.com/lookup?id=' + str(id_podcast))
        data = req.json()
        return data['results'][0]['feedUrl']