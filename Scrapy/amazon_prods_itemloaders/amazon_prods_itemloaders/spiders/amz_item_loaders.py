import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from amazon_prods_itemloaders.items import AmazonMacbooksItem


# def truncate_text(text):
#     return text[:50]


class MacbooksDetails(scrapy.Spider):
    name = 'amazon_product_scraper'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/s?k=macbook&ref=nb_sb_noss_2']

    # USE MUST CHANGE USER AGENTS IN SETTINGS TO GET SIMILAR RESULTS IN SHELL AND SPIDER
    def parse(self, response):
        search_results = response.css('div.a-spacing-medium')
        emptylist = []
        for result in search_results:
            product_loader = ItemLoader(item=AmazonMacbooksItem(), selector=result)
            # product_loader.default_input_processor = MapCompose(truncate_text)
            product_loader.default_output_processor = TakeFirst()
            if "Sponsored" not in result.css('div.a-spacing-micro > span::text').extract():
                if result.css('span.a-size-medium::text').extract() != emptylist:
                    product_loader.add_css('title', 'span.a-size-medium::text')
                    product_loader.add_css('current_price', 'span.a-price-whole::text')
                    product_loader.add_css('review', 'i.a-icon > span.a-icon-alt::text')
                    product_loader.add_css('no_of_reviews', 'span > a.a-link-normal > span.a-size-base::text')
                    product_loader.add_css('original_price', 'span.a-offscreen::text')
                    product_loader.add_css('link_to_product', 'h2.a-size-mini > a.a-link-normal::attr(href)')
                    yield product_loader.load_item()  # difference between yield and return is that yield doesnt exit the loop



