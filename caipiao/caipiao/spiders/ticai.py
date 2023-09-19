import scrapy
import json
from caipiao.items import CaipiaoItem
import uuid

class TicaiSpider(scrapy.Spider):
    """
    体彩开奖历史爬虫基类
    """
    name = 'ticai'
    allowed_domains = ['webapi.sporttery.cn']
    referer = 'https://static.sporttery.cn/'
    url = ''

    def start_requests(self):
        assert self.url != ''
        yield scrapy.Request(url=self.url+'1', headers={'Referer': self.referer}, callback=self.parse)

    def parseItem(self, data):
        pass
    
    def parse(self, response):
        data = json.loads(response.body)
        for d in data['value']['list']:
            yield self.parseItem(d)
        if data['value']['pageNo'] < data['value']['pages']:
            yield scrapy.Request(url=self.url+str(data['value']['pageNo']+1), headers={'Referer': self.referer}, callback=self.parse)

class TicaiDltSpider(TicaiSpider):
    """
    体彩大乐透
    """
    name = 'ticai_dlt'
    url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=100&isVerify=1&pageNo='

    def parseItem(self, d):
        numbers = d['lotteryDrawResult'].split(' ')
        item = CaipiaoItem()
        item['id'] = ''.join(str(uuid.uuid4()).split('-'))
        item['code'] = d['lotteryDrawNum']
        item['lottery_draw_date'] = d['lotteryDrawTime']
        item['lottery_draw_num1'] = ','.join(numbers[:-2])
        item['lottery_draw_num2'] = ','.join(numbers[-2:])
        item['lottery_type'] = 'dlt'
        item['result_json'] = json.dumps(d, ensure_ascii=False)
        return item

class TicaiPl3Spider(TicaiSpider):
    """
    体彩排列3
    """
    name = 'ticai_pl3'
    url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=35&provinceId=0&pageSize=100&isVerify=1&pageNo='

    def parseItem(self, d):
        item = CaipiaoItem()
        item['id'] = ''.join(str(uuid.uuid4()).split('-'))
        item['code'] = d['lotteryDrawNum']
        item['lottery_draw_date'] = d['lotteryDrawTime']
        item['lottery_draw_num1'] = d['lotteryDrawResult'].replace(' ', ',')
        item['lottery_draw_num2'] = ''
        item['lottery_type'] = 'pl3'
        item['result_json'] = json.dumps(d, ensure_ascii=False)
        return item

class TicaiPl5Spider(TicaiSpider):
    """
    体彩排列5
    """
    name = 'ticai_pl5'
    url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=350133&provinceId=0&pageSize=100&isVerify=1&pageNo='

    def parseItem(self, d):
        item = CaipiaoItem()
        item['id'] = ''.join(str(uuid.uuid4()).split('-'))
        item['code'] = d['lotteryDrawNum']
        item['lottery_draw_date'] = d['lotteryDrawTime']
        item['lottery_draw_num1'] = d['lotteryDrawResult'].replace(' ', ',')
        item['lottery_draw_num2'] = ''
        item['lottery_type'] = 'pl5'
        item['result_json'] = json.dumps(d, ensure_ascii=False)
        return item

class TicaiQxcSpider(TicaiSpider):
    """
    体彩七星彩
    """
    name = 'ticai_qxc'
    url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=04&provinceId=0&pageSize=100&isVerify=1&pageNo='

    def parseItem(self, d):
        numbers = d['lotteryDrawResult'].split(' ')
        item = CaipiaoItem()
        item['id'] = ''.join(str(uuid.uuid4()).split('-'))
        item['code'] = d['lotteryDrawNum']
        item['lottery_draw_date'] = d['lotteryDrawTime']
        item['lottery_draw_num1'] = ','.join(numbers[:-1])
        item['lottery_draw_num2'] = ','.join(numbers[-1:])
        item['lottery_type'] = 'qxc'
        item['result_json'] = json.dumps(d, ensure_ascii=False)
        return item
