import scrapy
from avatar.items import NicknameItem


class NicknameSpider(scrapy.Spider):
    name = 'nickname'
    allowed_domains = ['wxcha.com']
    start_urls = ['http://www.wxcha.com/wangming/update_1.html']

    def parse(self, response):
        names = response.css('.qm_wz>p::text').extract()
        for name in names:
            item = NicknameItem()
            item['name'] = name.strip()
            yield item

        next_page = response.css('.next::attr(href)').get()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)
