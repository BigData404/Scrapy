# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapynewsPipeline(object):
    def open_spider(self, spider):
        print('打开文件。。。。。。。。。')
        self.file = open('D:\ppppp\\news.txt','w',newline='')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        #itemStr = str(item).replace('[', '').replace(']', '')
        #itemStr = str(item['name']) + ',' + str(item['title']) + ',' + str(item['href']) + '\n'
        itemStr = str(item['title'])
        self.file.write(str(itemStr).replace('[', '').replace(']', '').replace("'", ""))
        return item
