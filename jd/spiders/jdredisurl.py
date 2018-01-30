# -*- coding: utf-8 -*-
import scrapy
from jd.items import RedisItem
import urllib.request
import re


class Ecspider(scrapy.Spider):
    name = 'jdspider'
    allowed_domains = ['jd.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'jd.pipelines.RedisPipeline': 300,
        }
    }
    start_urls = []
    for keywords in open('./keywords.txt', encoding='utf-8'):
        keyword = urllib.request.quote(keywords).replace('\\n', '')
        # 奇数页
        for i in range(1, 10, 2):
            start_urls.append(
                'https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page={}&s=1&click=0'.format(
                    str(keyword), str(i)))

    def parse(self, response):
        item = RedisItem()
        item['url'] = response.url
        yield item
