import scrapy
from avatar.items import AvatarItem


class WxchaSpider(scrapy.Spider):
    name = 'jj20'
    allowed_domains = ['jj20.com']
    start_urls = ['http://www.jj20.com/tx/']

    def parse(self, response):
        links = response.css('.g-class-top a::attr(href)')
        yield from response.follow_all(links, callback=self.parse_category)

    def parse_category(self, response):
        links = response.css('.g-select-img a::attr(href)')
        yield from response.follow_all(links, callback=self.parse_subject)

        next_page = response.css('.tsp_nav > i + a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_subject(self, response):
        imgs = response.css('#content img::attr(src)').extract()
        item = AvatarItem()
        item['image_urls'] = imgs
        yield item
