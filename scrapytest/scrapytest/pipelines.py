# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ScrapytestPipeline(object):

    def open_spider(self, spider):
        print('打开文件。。。。。。。。。')
        self.file = open('D:\ppppp\\网贷黑名单201812.txt','w',newline='')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        #itemStr = str(item).replace('[', '').replace(']', '')
        itemStr = str(item['title']) + '|' + str(item['cardID']) + '|' + str(item['phone']) + '|' + \
                  str(item['email']) + '|' + str(item['qq']) + '|' + str(item['name']) + '|' + str(item['amt']) + '|' + \
                  str(item['payamt']) + '|' + str(item['paylessamt']) + '|' + str(item['borrowtime']) + '|' + \
                  str(item['borrownumber']) + '|' + str(item['companyname']) + '|' + str(item['companyphone']) + '|' + \
                  str(item['companyaddress']) + '|' + str(item['addressphone']) + '|' + str(item['address']) + '|' + \
                  str(item['cardaddress']) + '|' + str(item['msgsource']) + '|' + str(item['msgsourcehttp']) + '|' + \
                  str(item['msgsourceupdatetime']) + '\n'
        self.file.write(str(itemStr).replace('[', '').replace(']', '').replace("'", ""))
        return item
