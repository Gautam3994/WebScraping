# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class MacbookCheck(object):
    def process_item(self, item, spider):
        if 'macbook' not in item['title'].lower() or float(item['current_price']) < 500:
            item['title'] = "Not a Macbook"
        return item


class PriceCheck(object):
    def process_item(self, item, spider):
        if float(item['current_price']) > 5000:
            item['current_price'] = "Expsenive"
        return item


class MarkAsViable(object):
    def process_item(self, item, spider):
        if item['title'] != 'Not a Macbook' and item['current_price'] != 'Expensive':
            print("\n\n------------OPTIONS-----------")
            # print("Link: ", item['link_to_product'])
            # print("Title: ", item['title'])
            # print("Price", item["current_price"], '--------------------------------\n')
        else:
            raise DropItem()
        return item

# ! AFTER MAKING CHANGES HERE GO TO SETTINGS
