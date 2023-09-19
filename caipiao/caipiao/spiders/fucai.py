import scrapy
import json
from caipiao.items import CaipiaoItem
import uuid
import re

class FucaiSpider(scrapy.Spider):
    """
    福彩开奖历史爬虫基类
    """
    name = 'fucai'
    allowed_domains = ['www.cwl.gov.cn']
    referer = 'http://www.cwl.gov.cn/ygkj/wqkjgg/ssq/'
    url = ''

    def start_requests(self):
        assert self.url != ''
        yield scrapy.Request(url=self.url+'1', headers={'Referer': self.referer}, dont_filter = True, callback=self.parse)

    def parseItem(self, data):
        pass
    
    def parse(self, response):
        data = json.loads(response.body)
        for d in data['result']:
            yield self.parseItem(d)
        if data['pageNo'] < data['pageNum']:
            yield scrapy.Request(url=self.url+str(data['pageNo']+1), headers={'Referer': self.referer}, dont_filter = True, callback=self.parse)

class FucaiSsqSpider(FucaiSpider):
    """
    福彩双色球
    """
    name = 'fucai_ssq'
    url = 'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&pageSize=100&systemType=PC&pageNo='

    def parseItem(self, d):
        item = CaipiaoItem()
        item['id'] = ''.join(str(uuid.uuid4()).split('-'))
        item['code'] = d['code']
        item['lottery_draw_date'] = re.findall(r'\d{4}-\d{2}-\d{2}', d['date'])[0]
        item['lottery_draw_num1'] = d['red']
        item['lottery_draw_num2'] = d['blue']
        item['lottery_type'] = 'ssq'
        item['result_json'] = json.dumps(d, ensure_ascii=False)
        return item

class FucaiQlcSpider(FucaiSpider):
    """
    福彩七乐彩
    """
    name = 'fucai_qlc'
    url = 'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=qlc&pageSize=100&systemType=PC&pageNo='

    def parseItem(self, d):
        item = CaipiaoItem()
        item['id'] = ''.join(str(uuid.uuid4()).split('-'))
        item['code'] = d['code']
        item['lottery_draw_date'] = re.findall(r'\d{4}-\d{2}-\d{2}', d['date'])[0]
        item['lottery_draw_num1'] = d['red']
        item['lottery_draw_num2'] = d['blue']
        item['lottery_type'] = 'qlc'
        item['result_json'] = json.dumps(d, ensure_ascii=False)
        return item

class FucaiFc3dSpider(FucaiSpider):
    """
    福彩3D
    """
    name = 'fucai_fc3d'
    url = 'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=3d&pageSize=100&systemType=PC&pageNo='

    def parseItem(self, d):
        item = CaipiaoItem()
        item['id'] = ''.join(str(uuid.uuid4()).split('-'))
        item['code'] = d['code']
        item['lottery_draw_date'] = re.findall(r'\d{4}-\d{2}-\d{2}', d['date'])[0]
        item['lottery_draw_num1'] = d['red']
        item['lottery_draw_num2'] = d['blue']
        item['lottery_type'] = 'fc3d'
        item['result_json'] = json.dumps(d, ensure_ascii=False)
        return item
