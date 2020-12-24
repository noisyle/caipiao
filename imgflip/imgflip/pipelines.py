# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class ImgflipPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        names = item['image_names']
        for i, url in enumerate(item['image_urls']):
            yield scrapy.Request(url, meta={'image_name': names[i]})

    def file_path(self, request, response=None, info=None, *, item=None):
        return f'full/%s.jpg' % request.meta['image_name']

    def thumb_path(self, request, thumb_id, response=None, info=None):
        return f'thumbs/{thumb_id}/%s.jpg' % request.meta['image_name']
