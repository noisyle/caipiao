import scrapy
from imgflip.items import ImgflipItem

class TemplateSpider(scrapy.Spider):
    name = 'template'
    allowed_domains = ['imgflip.com']
    start_urls = ['https://imgflip.com/memesearch?q=christmas']

    def parse(self, response):
        memes = response.css('.mt-img-wrap>a::attr(href)')
        yield from response.follow_all(memes, callback = self.parse_meme)

        next_page = response.css('a.pager-next::attr(href)')
        if next_page:
            yield from response.follow_all(next_page, callback = self.parse)


    def parse_meme(self, response):
        url = response.css('#mtm-img::attr(src)')
        if url:
            item = ImgflipItem()
            item['image_urls'] = [response.urljoin(url.get())]
            item['image_names'] = [response.css('#mtm-title::text').get()[:-9]]
            yield item