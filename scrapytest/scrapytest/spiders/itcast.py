from .requestType import *
from ..CourseItems import CourseItem
import scrapy
from scrapy.http import Request,FormRequest
import re
import time

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["dailianmeng.com"]

    def start_requests(self):
        url = 'http://dailianmeng.com/p2pblacklist/index.html?P2pBlacklist_page=0&ajax=yw0'
        return [Request(url, headers=get_headers(), callback=self.parse)]

    def parse(self, response):
        html = response.text
        hrefText = re.findall(r'target="_blank" href="(.+?)"', str(html))
        print(hrefText)
        print(len(hrefText))
        try:
            for docID in range(len(hrefText)):
                url_index = 'http://dailianmeng.com' + str(hrefText[docID])  # /p2pblacklist/view/QJJZ7v.html' print(url_index)
                self.logger.info('发送的url %s',url_index)
                time.sleep(1)
                '''进入详情页面'''
                yield scrapy.Request(url_index, headers=get_headers(), callback=self.getContent)
            next_page = response.xpath('//li[@class="next"]/a/@href').extract() #print(str(next_page))
            next_page_String = str(next_page).replace('[', '').replace(']', '').replace("'", "")
            if len(next_page_String) > 0:
                url_Child = 'http://dailianmeng.com' + str(next_page_String) #print(url_Child)
                self.logger.info('请求页面的url %s', url_Child)
                '''下一页'''
                yield scrapy.Request(url_Child, headers=get_headers(), callback=self.parse)
        except Exception as e:
            print('获取原文失败，保存url' + e)

    def getContent(self,response):
        self.logger.info('响应', response.text)
        item = CourseItem()
        item['title'] = response.xpath('//div[@class="row"]/div[@class="col-md-10"]/h1/text()').extract()
        item['cardID'] = response.xpath('//table[@class="detail-view table table-striped table-condensed"]/tr[1]/td/text()').extract()
        item['phone'] = response.xpath('//table[@id="yw0"]/tr[2]/td/text()').extract()
        item['email'] = response.xpath('//table[@id="yw0"]/tr[3]/td/text()').extract()
        item['qq'] = response.xpath('//table[@id="yw0"]/tr[4]/td/text()').extract()
        item['name'] = response.xpath('//table[@id="yw0"]/tr[5]/td/text()').extract()
        item['amt'] = response.xpath('//table[@id="yw0"]/tr[6]/td/text()').extract()
        item['payamt'] = response.xpath('//table[@id="yw0"]/tr[7]/td/text()').extract()
        item['paylessamt'] = response.xpath('//table[@id="yw0"]/tr[8]/td/text()').extract()
        item['borrowtime'] = response.xpath('//table[@id="yw0"]/tr[9]/td/text()').extract()
        item['borrownumber'] = response.xpath('//table[@id="yw0"]/tr[10]/td/text()').extract()
        item['companyname'] = response.xpath('//table[@id="yw0"]/tr[11]/td/text()').extract()
        item['companyphone'] = response.xpath('//table[@id="yw0"]/tr[12]/td/text()').extract()
        item['companyaddress'] = response.xpath('//table[@id="yw0"]/tr[13]/td/text()').extract()
        item['addressphone'] = response.xpath('//table[@id="yw0"]/tr[14]/td/text()').extract()
        item['address'] = response.xpath('//table[@id="yw0"]/tr[15]/td/text()').extract()
        item['cardaddress'] = response.xpath('//table[@id="yw0"]/tr[16]/td/text()').extract()
        item['msgsource'] = response.xpath('//table[@id="yw0"]/tr[17]/td/text()').extract()
        item['msgsourcehttp'] = response.xpath('//table[@id="yw0"]/tr[18]/td/text()').extract()
        item['msgsourceupdatetime'] = response.xpath('//table[@id="yw0"]/tr[19]/td/text()').extract()
        #item['title'] = response.xpath('//div[@class="row"]/div[@class="col-md-10"]/h1').re('h1\>(.*?)\<\/h1')
        yield item
