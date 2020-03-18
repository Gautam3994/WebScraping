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


