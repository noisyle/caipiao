import scrapy
from lengyue.items import LengyueItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['v.lengyue.app']
    start_urls = [
        u'https://v.lengyue.app/index.php/vod/type/id/1.html',
        u'https://v.lengyue.app/index.php/vod/type/id/2.html',
        u'https://v.lengyue.app/index.php/vod/type/id/3.html',
        u'https://v.lengyue.app/index.php/vod/type/id/4.html',
        u'https://v.lengyue.app/index.php/vod/type/id/34.html',
        u'https://v.lengyue.app/index.php/vod/type/id/66.html',
    ]

    def parse(self, response):
        names = response.css('.module-item .module-item-title::text').extract()
        for name in names:
            item = LengyueItem()
            item['name'] = name.strip()
            yield item

        try:
            pager = response.css('#page').get()
            if pager:
                next = response.css('.page-number.display')[-1].attrib['href']
                yield response.follow(next, callback=self.parse)
        except KeyError:
            pass
