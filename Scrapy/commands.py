"""
scrapy - to see avaiable commands

1) Benchmarking - scrapy bench
2) Fetch HTML - scrapy fetch --nolog https://app.pluralsight.com/id/
3)Project specific settings - scrapy settings
4)To see how scrapy view html content - scrapy view https://www.youtube.com/
NORMALLY SCRAPY CAN DISPLAY ONLY STATIC CONTENT - YOU NEED TO INSTALL FLASH CONTENT TO VIEW DYNAMIC CONTENT

SCRAPY SHELL

scrapy shell http://quotes.toscrape.com/
scrapy shell is basically like python shell

shelp() 'help'
request 'determines to type of HTTP request'
response.url 'url'
response.text 'html'
response.status
response.headers
dir(response) to know others
view(repsonse) to see how it looks in the browser
items - to store data in structured format
settings.get('BOT_NAME')
spider

fetch('http://quotes.toscrape.com/page/2')
fetch('https://www.un.org')
file:///C:/Users/Gautam/AppData/Local/Temp/tmpjvohmmy4.html

SCRAPY ALSO WORKS WITH HTML PRESENT IN LOCAL TOO
USE exit() to get out of shell

scrapy shell file:///C:/Users/Gautam/AppData/Local/Temp/tmpjvohmmy4.html

"""

"""SIMPLE SCRAPING USING CSS SELECTORS

scrapy shell http://quotes.toscrape.com/

USING TAGS
response.css('title')
response.css('title').extract()
response.css('title::text').extract() 

USING CLASSES
response.css('.author')
response.css('.author').extract()
response.css('.author::text').extract() # this returns a list

TO ACCESS INDIVIDUAL ELEMENTS USE
response.css('.author::text').extract()[0]
OR
response.css('.author::text').extract_first()

COMBINING TAGS AND CLASSES
response.css('small.author::text').extract()
response.css('span.text::text').extract_first()
response.css('span.text::text').extract()

NESTED TAGS AND CLASSES
response.css('div.quote > span.text::text').extract()

#! TO SELECT CSS ELEMENT RIGHT CLICK ON THE TAG COPY - COPY SELECTOR
body > div > div:nth-child(2) > div.col-md-8 > div:nth-child(1) > span.text

FOR STRING WITH TAGS
response.css("body > div > div:nth-child(2) > div.col-md-8 > div:nth-child(2) > span.text").extract()
FOR TEXT ALONE
response.css("body > div > div:nth-child(2) > div.col-md-8 > div:nth-child(2) > span.text::text").extract() 
 
TO LOOP CHANGE nth child
response.css("body > div > div:nth-child(2) > div.col-md-8 > div:nth-child(3) > span.text::text").extract() 


response.css('body > div > div:nth-child(2) > div.col-md-8 > div:nth-child(1) > span:nth-child(2) > a').extract()

GET ATTRIBUTES - FOR ONE ELEMENT
response.css('body > div > div:nth-child(2) > div.col-md-8 > div:nth-child(1) > span:nth-child(2) > a::attr(href)').extract()

FOR ALL LINKS
response.css('a::attr(href)').extract()
response.css('div::attr(data-cel-widget)').extract() 

"""

"""
SIMPLE SCRAPING USING XPATH

response.xpath('/html/head/title').extract()
response.xpath('/html/head/title/text()').extract()

TO SEARCH ANYWHERE
response.xpath('//title/text()').extract()

GET ONE AUTHORS USING XPATH
response.xpath("").extract()
response.xpath("/html/body/div/div[2]/div[1]/div[5]/span[2]/small").extract()
response.xpath("/html/body/div/div[2]/div[1]/div[5]/span[2]/small/text()").extract()

TO GET ALL AUTHORS - JUST REMOVE ELEMENT INDICATORS
response.xpath("/html/body/div/div/div/div/span/small/text()").extract()

PARTICULAR QUOTE
response.xpath("/html/body/div/div[2]/div[1]/div[4]/span[1]/text()")

COMBINING CSS CLASS WITH XPATH
response.xpath("//span[@class='text']").extract()
response.xpath("//span[@class='text']/text()").extract()

FOR ALL LINKS
response.xpath("//a/@href").extract()

TO LEARN MORE SEE BEAUTIFUL_XML PYTHON NOTEBOOK


"""

"""
REGEX WITH CSS AND XPATH
This is page 2 in quotespage

response.xpath("//*[contains(text(), 'friend')]/text()") - * represents all tags
response.xpath("//*[contains(text(), 'friend')]").extract()

'Below only returns quotes'
response.css(".text:contains('friend')::text").extract()

'ALL AUTHORS WHOSE NAME STARTS WITH A'
response.css(".author::text").re('A[a-z]*\s\w+')
response.xpath("//*[@class='author'][starts-with(text(), 'A')]/text()").extract()
"""
