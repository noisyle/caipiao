import scrapy
import json
from caipiao.items import CaipiaoItem
import re
import uuid

class FucaiSsqSpider(scrapy.Spider):
    """
    福彩双色球
    """
    name = 'fucai_ssq'
    allowed_domains = ['www.cwl.gov.cn']
    referer = 'http://www.cwl.gov.cn/kjxx/ssq/kjgg/'

    def start_requests(self):
        urls = [
            'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=100',
        ]

        for url in urls:
            yield scrapy.Request(url=url, headers={'Referer': self.referer}, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        print(data['result'][0])
        for d in data['result']:
            item = CaipiaoItem()
            item['id'] = ''.join(str(uuid.uuid4()).split('-'))
            item['code'] = d['code']
            item['lottery_draw_date'] = re.findall(r'\d{4}-\d{2}-\d{2}', d['date'])[0]
            item['lottery_draw_num1'] = d['red']
            item['lottery_draw_num2'] = d['blue']
            item['lottery_type'] = 'ssq'
            item['result_json'] = json.dumps(d, ensure_ascii=False)
            yield item


class FucaiQlcSpider(scrapy.Spider):
    """
    福彩七乐彩
    """
    name = 'fucai_qlc'
    allowed_domains = ['www.cwl.gov.cn']
    referer = 'http://www.cwl.gov.cn/kjxx/qlc/kjgg/'

    def start_requests(self):
        urls = [
            'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=qlc&issueCount=100',
        ]

        for url in urls:
            yield scrapy.Request(url=url, headers={'Referer': self.referer}, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        print(data['result'][0])
        for d in data['result']:
            item = CaipiaoItem()
            item['id'] = ''.join(str(uuid.uuid4()).split('-'))
            item['code'] = d['code']
            item['lottery_draw_date'] = re.findall(r'\d{4}-\d{2}-\d{2}', d['date'])[0]
            item['lottery_draw_num1'] = d['red']
            item['lottery_draw_num2'] = d['blue']
            item['lottery_type'] = 'qlc'
            item['result_json'] = json.dumps(d, ensure_ascii=False)
            yield item

class FucaiFc3dSpider(scrapy.Spider):
    """
    福彩七乐彩
    """
    name = 'fucai_fc3d'
    allowed_domains = ['www.cwl.gov.cn']
    referer = 'http://www.cwl.gov.cn/kjxx/3d/kjgg/'

    def start_requests(self):
        urls = [
            'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=3d&issueCount=100',
        ]

        for url in urls:
            yield scrapy.Request(url=url, headers={'Referer': self.referer}, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        print(data['result'][0])
        for d in data['result']:
            item = CaipiaoItem()
            item['id'] = ''.join(str(uuid.uuid4()).split('-'))
            item['code'] = d['code']
            item['lottery_draw_date'] = re.findall(r'\d{4}-\d{2}-\d{2}', d['date'])[0]
            item['lottery_draw_num1'] = d['red']
            item['lottery_draw_num2'] = d['blue']
            item['lottery_type'] = 'fc3d'
            item['result_json'] = json.dumps(d, ensure_ascii=False)
            yield item