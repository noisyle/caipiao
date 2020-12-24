import scrapy
from avatar.items import AvatarItem


class WxchaSpider(scrapy.Spider):
    name = 'wxcha'
    allowed_domains = ['wxcha.com']
    start_urls = ['http://www.wxcha.com/touxiang/update_1.html']

    def parse(self, response):
        links = response.css('.wz::attr(href)').extract()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_link)

        next_page = response.css('.next::attr(href)').get()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_link(self, response):
        imgs = response.css('.cl img::attr(data-src)').extract()
        item = AvatarItem()
        item['image_urls'] = imgs
        yield item

        
