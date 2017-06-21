import scrapy
import json
import urllib.parse
from ..items import RootspiderItem

class RootSpider(scrapy.Spider):
    name = "root"
    character = scrapy.Field()

    def __init__(self, c=None, *args, **kwargs):
        super(RootSpider, self).__init__(*args, **kwargs)
        self.character = c

    def start_requests(self):
        url = "http://www.chaiwubi.com/bmcx"
        yield scrapy.http.FormRequest(url, formdata={'wz': self.character, 'select_value': '查单字'}, callback=self.parse)

    def parse(self, response):
        item86 = RootspiderItem()
        item86["character"] = self.character
        item86["code1"] = response.xpath("//body/div/div/div/div/table/tr/td/strong[contains(@title, '王码86版一级简码')]/text()").extract_first()
        item86["code2"] = response.xpath("//body/div/div/div/div/table/tr/td/strong[contains(@title, '王码86版二级简码')]/text()").extract_first()
        item86["code3"] = response.xpath("//body/div/div/div/div/table/tr/td/strong[contains(@title, '王码86版三级简码')]/text()").extract_first()
        item86["code4"] = response.xpath("//body/div/div/div/div/table/tr/td/strong[contains(@title, '王码86版全码')]/text()").extract_first()
        item86["version"] = "86"
        item86["img_url"] = response.xpath("//body/div/div/div/div/table/tr/td/div/img[contains(@src, 'http://att.chaiwubi.com/wubi/86tj/')]/@src").extract_first()
        file86 = open("./item/"+self.character+"_86.json", 'w')
        line86 = json.dumps(dict(item86), ensure_ascii=False) + "\n"
        file86.write(line86)

        item98 = RootspiderItem()
        item98["character"] = self.character
        item98["code1"] = response.xpath("//body/div/div/div/div/table/tr/td/strong[contains(@title, '王码98版一级简码')]/text()").extract_first()
        item98["code2"] = response.xpath("//body/div/div/div/div/table/tr/td/strong[contains(@title, '王码98版二级简码')]/text()").extract_first()
        item98["code3"] = response.xpath("//body/div/div/div/div/table/tr/td/strong[contains(@title, '王码98版三级简码')]/text()").extract_first()
        item98["code4"] = response.xpath("//body/div/div/div/div/table/tr/td/strong[contains(@title, '王码98版全码')]/text()").extract_first()
        item98["version"] = "98"
        item98["img_url"] = response.xpath("//body/div/div/div/div/table/tr/td/div/img[contains(@src, 'http://att.chaiwubi.com/wubi/98tj/')]/@src").extract_first()
        file98 = open("./item/"+self.character+"_98.json", 'w')
        line98 = json.dumps(dict(item98), ensure_ascii=False) + "\n"
        file98.write(line98)

        yield scrapy.Request(item86["img_url"], callback=self.img_save)
        yield scrapy.Request(item98["img_url"], callback=self.img_save)

    def img_save(self, response):
        character = urllib.parse.unquote(response.url.split("/")[-1][0:-4])
        version = response.url.split("/")[-2][0:2]
        file_name = character + "_"+version+".gif"
        file = open("./img/"+file_name, 'wb')
        file.write(response.body)