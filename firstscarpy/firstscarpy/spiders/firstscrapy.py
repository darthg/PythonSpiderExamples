# -*- coding: utf-8 -*-
import scrapy
from firstscarpy.items import FirstscarpyItem
#由genspider生成

class FirstscrapySpider(scrapy.Spider):
    name = 'firstscrapy'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        item=FirstscarpyItem()
        item["content"]=response.xpath("/html/head/title/text()").extract()
        yield item