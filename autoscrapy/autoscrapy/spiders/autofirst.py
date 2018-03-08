# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from autoscrapy.items import AutoscrapyItem   #导入容器
from scrapy.http import Request

class AutofirstSpider(CrawlSpider):
    name = 'autofirst'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']

    rules = (
        Rule(LinkExtractor(allow=r'article'), callback='parse_item', follow=True),#follow=True链接是否跟进，false的话就爬一次
    )#链接提取的规律

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
