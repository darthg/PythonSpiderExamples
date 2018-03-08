# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstscarpyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     content=scrapy.Field()#创建名为content的容器
     link=scrapy.Field()
