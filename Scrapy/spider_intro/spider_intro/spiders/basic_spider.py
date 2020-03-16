"""
Command
C:\Users\Gautam\WebScraping\Scrapy\
scrapy startproject spider_intro
"""

import scrapy


class IntroSpider(scrapy.Spider):
    name = "basic_spider"  # !THIS NAME IS VERY IMPORTANT

    def start_requests(self):
        for i in range(5):
            yield scrapy.Request(url=f"http://books.toscrape.com/catalogue/page-{i + 1}.html")

    def parse(self, response):
        book_list = response.xpath('//*[@id="default"]/div/div/div/div/section/div/ol/li/article/h3/a/@title').extract()
        print(book_list)
        with open('title_of_books_in_first_5.txt', 'a+') as title_file:
            for book_title in book_list:
                title_file.write(book_title + "\n")


"""
After in the two level below where you used scrapy start project(C:\Users\Gautam\WebScraping\Scrapy\spider_intro\spider_intro>)
use scrapy crawl basic
"""
# https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html