import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SimpleSpiderCrawl(CrawlSpider):  # crawl spider is used to crawl all links in a website
    name = 'simple_crawler'

    allowed_domains = ['un.org']
    start_urls = ['https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html']
    rules = (Rule(LinkExtractor(allow='funds-programmes-specialized-agencies-and-others', deny=('ar/sections')), callback='parse_page'),)  # for every page parse_page func wil be called

    def parse_page(self, response):
        list_of_agencies = response.xpath('//*[@id="node-5271"]/div/div/div/div/h4/text()').extract()
        for agency in list_of_agencies:
            with open('un_agencies.txt', 'a+', encoding='utf-8') as agency_file:
                agency_file.write(agency + '\n')
