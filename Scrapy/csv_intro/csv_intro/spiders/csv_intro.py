from scrapy.spiders import CSVFeedSpider


class CsvSpider(CSVFeedSpider):
    name = "csv_spider"

    start_urls = ['https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv']
    # WE GET BELOW DETAILS BY FOLLOWING THE LINK
    delimiter = ';'
    quotechar = '"'

    headers = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide",
               "total sulfur dioxide",
               "density", "pH", "sulphates", "alcohol", "quality"]

    def parse_row(self, response, row):
        print(f'pH={row["pH"]},\tAlcohol Content={row["alcohol"]}, \tWineQuality={row["quality"]}')

"""

"""
scrapy shell -s USER_AGENT="""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36""" "https://www.amazon.in/s?k=macbook&ref=nb_sb_noss_2"
response.css('span.a-size-medium::text').extract()
response.xpath('//a/span[@class="a-size-medium a-color-base a-text-normal"]').extract()

Removing ads
# Below lets us know if it is a add
response.css('div.a-spacing-micro > span::text').extract()
