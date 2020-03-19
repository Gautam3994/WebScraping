# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose


def process_url(value):
    domain = "https://stackoverflow.com"
    complete_url = domain + value
    return complete_url


class StackoverflowLoggingItem(scrapy.Item):
    question = scrapy.Field()
    url = scrapy.Field(input_processor=MapCompose(process_url))
