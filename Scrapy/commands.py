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

fetch('https://www.un.org')
file:///C:/Users/Gautam/AppData/Local/Temp/tmpjvohmmy4.html

SCRAPY ALSO WORKS WITH HTML PRESENT IN LOCAL TOO
USE exit() to get out of shell

scrapy shell file:///C:/Users/Gautam/AppData/Local/Temp/tmpjvohmmy4.html

"""
