import scrapy
from stackoverflow_logging.items import StackoverflowLoggingItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class LogSpider(scrapy.Spider):

    name = 'logger'
    start_urls = ['https://stackoverflow.com/questions?sort=featured']

    def parse(self, response):

        questions = response.css('div.summary')

        if len(questions) == 0:
            self.logger.error("No elements found on this page")

        self.logger.info("loading the item into the scraper")

        for question in questions:
            loader_object = ItemLoader(item=StackoverflowLoggingItem(), selector=question)
            loader_object.default_output_processor = TakeFirst()

            self.logger.debug("Adding data to the item loader object")

            loader_object.add_css('question', 'h3 > a.question-hyperlink::text')
            loader_object.add_css('url', 'h3 > a.question-hyperlink::attr(href)')

            yield loader_object.load_item()
