# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class GoogleMapsPipeline(object):
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline(object):
 
    def __init__(self):
        self.currency_seen = set()
 
    def process_item(self, item, spider):
        if item['Name'] in self.currency_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.currency_seen.add(item['Name'])
            return item