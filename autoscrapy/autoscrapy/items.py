# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutoscrapyItem(scrapy.Item):#编辑容器内传递的数据
    content=scrapy.Field()
    link=scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()

