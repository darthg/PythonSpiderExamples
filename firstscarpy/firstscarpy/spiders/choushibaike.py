# -*- coding: utf-8 -*-
import scrapy
from firstscarpy.items import FirstscarpyItem
from scrapy.http import Request

class ChoushibaikeSpider(scrapy.Spider):
    name = 'choushibaike'
    allowed_domains = ['qiushibaike.com']
    #start_urls = ['http://qiushibaike.com/']
    def start_requests(self):
         url="http://www.qiushibaike.com/"
         ua={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"}
         yield Request(url,headers=ua)
    def parse(self, response):
          it=FirstscarpyItem()
          it["content"]=response.xpath("//div[@class='content']/span/text()").extract()
          it["link"]=response.xpath("//a[@class='contentHerf']/@href").extract()
          yield it
