# # Shell commands
# scrapy shell -s USER_AGENT="""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36""" "https://www.amazon.in/s?k=macbook&ref=nb_sb_noss_2"
# response.css('span.a-size-medium::text').extract()
# response.xpath('//a/span[@class="a-size-medium a-color-base a-text-normal"]').extract()
#
# Removing ads
# # Below lets us know if it is a add
# response.css('div.a-spacing-none > div.a-spacing-micro > span::text').extract()
# response.css('div.a-spacing-none > * > * > span.a-size-medium::text').extract()
# type(response.css('div.a-spacing-none').extract())
# main_div = response.css('div.a-spacing-medium')
# emptylist = []
# for single_div in main_div:
#     if not "Sponsored" in single_div.css('div.a-spacing-micro > span::text').extract():
#         if single_div.css('span.a-size-medium::text').extract() != emptylist:
#             product1['title'] = single_div.css('span.a-size-medium::text').extract()[0]
#             product1['current_price'] = single_div.css('span.a-price-whole::text').extract()[0]
#             product1['review'] = single_div.css('i.a-icon > span.a-icon-alt::text').extract()[0]
#             product1['no_of_reviews'] = single_div.css('span > a.a-link-normal > span.a-size-base::text').extract()[0]
#             product1['original_price'] = single_div.css('span.a-offscreen::text').extract()[1]
#             product1['link_to_product'] = "https://amazon.in"+single_div.css('h2.a-size-mini > a.a-link-normal::attr(href)').extract()[0]
#             break
#
# #Storing values in items(items are like dictionaries)
# #Remember you cant add new fields like in normal dict first you have to add it here
# class ProductItem(scrapy.Item):
#     title = scrapy.Field()
#     current_price = scrapy.Field()
#     review = scrapy.Field()
#     no_of_reviews = scrapy.Field()
#     original_price = scrapy.Field()
#     link_to_product = scrapy.Field()
#
# product1 = ProductItem()