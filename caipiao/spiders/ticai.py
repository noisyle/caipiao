import scrapy
import json
from caipiao.items import CaipiaoItem
import re
import uuid


class TicaiDltSpider(scrapy.Spider):
    """
    体彩大乐透
    """
    name = 'ticai_dlt'
    allowed_domains = ['webapi.sporttery.cn']
    referer = 'https://static.sporttery.cn/'

    def start_requests(self):
        urls = [
            'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=100&isVerify=1&pageNo=1',
        ]

        for url in urls:
            yield scrapy.Request(url=url, headers={'Referer': self.referer}, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        print(data['value']['list'][0])
        for d in data['value']['list']:
            numbers = d['lotteryDrawResult'].split(' ')
            item = CaipiaoItem()
            item['id'] = ''.join(str(uuid.uuid4()).split('-'))
            item['code'] = d['lotteryDrawNum']
            item['lottery_draw_date'] = d['lotteryDrawTime']
            item['lottery_draw_num1'] = ','.join(numbers[:-2])
            item['lottery_draw_num2'] = ','.join(numbers[-2:])
            item['lottery_type'] = 'dlt'
            item['result_json'] = json.dumps(d, ensure_ascii=False)
            yield item

class TicaiPl3Spider(scrapy.Spider):
    """
    体彩排列3
    """
    name = 'ticai_pl3'
    allowed_domains = ['webapi.sporttery.cn']
    referer = 'https://static.sporttery.cn/'

    def start_requests(self):
        urls = [
            'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=35&provinceId=0&pageSize=100&isVerify=1&pageNo=1',
        ]

        for url in urls:
            yield scrapy.Request(url=url, headers={'Referer': self.referer}, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        print(data['value']['list'][0])
        for d in data['value']['list']:
            item = CaipiaoItem()
            item['id'] = ''.join(str(uuid.uuid4()).split('-'))
            item['code'] = d['lotteryDrawNum']
            item['lottery_draw_date'] = d['lotteryDrawTime']
            item['lottery_draw_num1'] = d['lotteryDrawResult'].replace(' ', ',')
            item['lottery_draw_num2'] = ''
            item['lottery_type'] = 'pl3'
            item['result_json'] = json.dumps(d, ensure_ascii=False)
            yield item

class TicaiPl5Spider(scrapy.Spider):
    """
    体彩排列5
    """
    name = 'ticai_pl5'
    allowed_domains = ['webapi.sporttery.cn']
    referer = 'https://static.sporttery.cn/'

    def start_requests(self):
        urls = [
            'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=350133&provinceId=0&pageSize=100&isVerify=1&pageNo=1',
        ]

        for url in urls:
            yield scrapy.Request(url=url, headers={'Referer': self.referer}, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        print(data['value']['list'][0])
        for d in data['value']['list']:
            item = CaipiaoItem()
            item['id'] = ''.join(str(uuid.uuid4()).split('-'))
            item['code'] = d['lotteryDrawNum']
            item['lottery_draw_date'] = d['lotteryDrawTime']
            item['lottery_draw_num1'] = d['lotteryDrawResult'].replace(' ', ',')
            item['lottery_draw_num2'] = ''
            item['lottery_type'] = 'pl5'
            item['result_json'] = json.dumps(d, ensure_ascii=False)
            yield item

class TicaiQxcSpider(scrapy.Spider):
    """
    体彩七星彩
    """
    name = 'ticai_qxc'
    allowed_domains = ['webapi.sporttery.cn']
    referer = 'https://static.sporttery.cn/'

    def start_requests(self):
        urls = [
            'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=04&provinceId=0&pageSize=100&isVerify=1&pageNo=1',
        ]

        for url in urls:
            yield scrapy.Request(url=url, headers={'Referer': self.referer}, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        print(data['value']['list'][0])
        for d in data['value']['list']:
            numbers = d['lotteryDrawResult'].split(' ')
            item = CaipiaoItem()
            item['id'] = ''.join(str(uuid.uuid4()).split('-'))
            item['code'] = d['lotteryDrawNum']
            item['lottery_draw_date'] = d['lotteryDrawTime']
            item['lottery_draw_num1'] = ','.join(numbers[:-1])
            item['lottery_draw_num2'] = ','.join(numbers[-1:])
            item['lottery_type'] = 'qxc'
            item['result_json'] = json.dumps(d, ensure_ascii=False)
            yield item
