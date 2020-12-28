# - coding: utf8 -
import scrapy
from avatar.items import AvatarItem
import json


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = [u'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&word=中老年人头像&pn=%d&rn=30' % (i*30) for i in range(1,101)]

    def parse(self, response):
        data = json.loads(response.body)['data']
        for row in data:
            if 'middleURL' in row:
                item = AvatarItem()
                item['image_urls'] = [row['middleURL']]
                yield item
