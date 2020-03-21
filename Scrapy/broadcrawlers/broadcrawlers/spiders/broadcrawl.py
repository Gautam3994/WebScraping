import re
import csv

import scrapy
from scrapy.loader import ItemLoader
from w3lib.html import replace_escape_chars
from scrapy.loader.processors import MapCompose
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from broadcrawlers.items import BroadcrawlersItem


class BroadCrawler(CrawlSpider):
    name = "broad_crawler"
    start_urls = [
        "http://www.columbia.edu/",
        "https://www.espn.com",
        # "https://www.loonycorn.in",
        # "https://www.paytm.in"
    ]

    rules = (Rule(LinkExtractor(), callback="parse_item"),)

    def parse_item(self, response):
        loader_object = ItemLoader(item=BroadcrawlersItem(), response=response)
        loader_object.default_output_processor = MapCompose(lambda x: x.strip(),
                                                            replace_escape_chars)  # WE ARE SPECIFYING MULTIPLE FUNCTIONS HERE USING COMMAS
        emails = response.xpath("//text()").re(
            r'(?!\S*\.(?:jpg|png|gif|bmp)(?:[\s\n\r]|$))[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]{3,65}\.[A-Za-z]{2,4}')
        # https://stackoverflow.com/questions/37892578/how-to-exclude-images-from-regex-email-extraction #THIS IS A SAMPLE DONT USE IT WITHOUT TESTING
        # (r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        # r'[a-zA-Z0-9.-]+@[a-z-]+\.(com|edu|net)')
        if emails:
            loader_object.add_value('email', emails)
            loader_object.add_value('url', response.url)

        return loader_object.load_item()
        # NOTE THE FILE MUST BE CLOSED BEFORE RUNNING THE PROGRAM IF YOU ARE APPENDING
