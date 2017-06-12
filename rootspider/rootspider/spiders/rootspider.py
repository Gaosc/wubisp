import scrapy

class RootSpider(scrapy.Spider):
    name = "root_spider"
    start_urls = ["http://www.baidu.com/",
                  "http://www.360.com/"]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)