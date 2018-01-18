#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RedisItem(scrapy.Item):
    url = scrapy.Field()

class MongodbItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    pid = scrapy.Field()
    shuxing = scrapy.Field()

class MongodbCommentItem(scrapy.Item):
    pid = scrapy.Field()
    comment = scrapy.Field()
    pubtime = scrapy.Field()