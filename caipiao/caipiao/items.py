# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CaipiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    code = scrapy.Field()
    lottery_draw_date = scrapy.Field()
    lottery_draw_num1 = scrapy.Field()
    lottery_draw_num2 = scrapy.Field()
    lottery_type = scrapy.Field()
    result_json = scrapy.Field()
