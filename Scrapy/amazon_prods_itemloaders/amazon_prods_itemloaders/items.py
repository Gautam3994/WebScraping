# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose

USD_INR = 74.40


def convert_price(price):
    if price:
        return float(price.replace(",", '').replace("₹", '')) / USD_INR


def shorten_link(full_link):
    product_id = full_link.split("/")[-2]
    return "https://amazon.in/dp/" + product_id


class TakeSecond(object):
    def __call__(self, values):
        for i in range(len(values)):
            if i == 1:
                if values[i] is not None and values[i] != '':
                    return values[i]


class AmazonMacbooksItem(scrapy.Item):
    title = scrapy.Field()
    current_price = scrapy.Field(input_processor=MapCompose(convert_price))
    review = scrapy.Field()
    no_of_reviews = scrapy.Field()
    original_price = scrapy.Field(input_processor=MapCompose(convert_price), output_processor=TakeSecond())
    link_to_product = scrapy.Field(input_processor=MapCompose(shorten_link))

