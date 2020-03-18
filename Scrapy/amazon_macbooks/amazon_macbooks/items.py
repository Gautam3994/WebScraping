# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonMacbooksItem(scrapy.Item):
    title = scrapy.Field()
    current_price = scrapy.Field()
    review = scrapy.Field()
    no_of_reviews = scrapy.Field()
    original_price = scrapy.Field()
    link_to_product = scrapy.Field()
