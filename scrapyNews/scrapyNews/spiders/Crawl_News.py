# -*- coding: utf-8 -*-#

# Name:         Crawl_News.py
# Author:       jiaocheng
# Date:         2018/12/11
# Description:
import scrapy
from scrapy.http import Request,FormRequest
from scrapyNews.items import ScrapynewsItem
from scrapyNews.spiders.requestType import *
import re
from bs4 import BeautifulSoup

class crawl_News(scrapy.Spider):
    name = 'news'
    allowed_domains = ["news.163.com"]
    item = ScrapynewsItem()

    def start_requests(self):
        url = 'http://news.163.com/rank/'
        return [Request(url,headers=get_headers(), callback=self.parse)]

    def parse(self, response):
        r = response.text
        mypage_Info = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>',response.text, re.S)
        for i in range(len(mypage_Info)):
             if i == 0 : continue
             #if i == 2: break
             print(str(mypage_Info[i][0]),str(mypage_Info[i][1]))
             self.item['name'] = str(mypage_Info[i][0])
             yield scrapy.Request(mypage_Info[i][1], headers=get_headers(), callback=self.getContent)

    def getContent(self,response):
        name = re.findall(r'<div class="titleBar"><h2>(.*?)</h2><div class="more">', str(response.text))
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find(class_='area-half left')
        div2 = div.find(class_='tabContents active')
        tr = div2.find_all('tr')
        line = self.getMsg(tr,name[0])
        self.item['title'] = str(line)
        yield self.item

    def getMsg(self,list,name):
        line = ""
        msgLine = re.findall(r'<td class=".*?"><span>(.*?)</span><a href="(.*?)">(.*?)</a></td>', str(list))
        msgLine_more = re.findall(r'<td class="(.*?)"><a href="(.*?)">(.*?)</a></td>', str(list))
        #print(msgLine_more)
        msgLine = msgLine + msgLine_more
        for i in range(len(msgLine)):
            one_line = str(name) + ',' + str(i+1) + ',' + msgLine[i][1] + ',' + msgLine[i][2] + '\n'
            line = line + one_line
        return line



