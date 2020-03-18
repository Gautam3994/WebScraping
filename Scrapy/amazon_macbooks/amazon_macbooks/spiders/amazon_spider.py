import scrapy
from amazon_macbooks.items import AmazonMacbooksItem


class MacbooksDetails(scrapy.Spider):
    name = 'amazon_product_scraper'
    allowed_domains = ['www.amazon.in/s?k=macbook&ref=nb_sb_noss_2']
    start_urls = ['https://www.amazon.in/s?k=macbook&ref=nb_sb_noss_2']

    # USE MUST CHANGE USER AGENTS IN SETTINGS TO GET SIMILAR RESULTS IN SHELL AND SPIDER
    def parse(self, response):
        search_results = response.css('div.a-spacing-medium')
        emptylist = []
        macbook = AmazonMacbooksItem()
        for result in search_results:
            if "Sponsored" not in result.css('div.a-spacing-micro > span::text').extract():
                if result.css('span.a-size-medium::text').extract() != emptylist:
                    macbook = AmazonMacbooksItem()
                    macbook['title'] = result.css('span.a-size-medium::text').extract()[0]
                    macbook['current_price'] = result.css('span.a-price-whole::text').extract()[0]
                    macbook['review'] = result.css('i.a-icon > span.a-icon-alt::text').extract()[0]
                    macbook['no_of_reviews'] = result.css('span > a.a-link-normal > span.a-size-base::text').extract()[0]
                    macbook['original_price'] = result.css('span.a-offscreen::text').extract()[1]
                    macbook['link_to_product'] = "https://amazon.in" + result.css(
                        'h2.a-size-mini > a.a-link-normal::attr(href)').extract()[0]
                    yield macbook  # difference between yield and return is that yield doesnt exit the loop



