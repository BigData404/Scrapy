#引入文件
import scrapy


class CourseItem(scrapy.Item):

    title = scrapy.Field()
    #身份证号
    cardID = scrapy.Field()
    #手机号
    phone = scrapy.Field()
    #email
    email = scrapy.Field()
    #qq
    qq = scrapy.Field()
    # 姓名
    name = scrapy.Field()
    # 本金/本息
    amt = scrapy.Field()
    # 已还金额
    payamt = scrapy.Field()
    # 未还/罚息
    paylessamt = scrapy.Field()
    # 借款时间
    borrowtime = scrapy.Field()
    # 借款期数
    borrownumber = scrapy.Field()
    # 公司名称
    companyname = scrapy.Field()
    # 公司电话
    companyphone = scrapy.Field()
    # 公司地址
    companyaddress = scrapy.Field()
    # 居住电话
    addressphone = scrapy.Field()
    # 居住地址
    address = scrapy.Field()
    # 证件地址
    cardaddress = scrapy.Field()
    # 信息来源
    msgsource = scrapy.Field()
    # 信息来源网址
    msgsourcehttp = scrapy.Field()
    # 信息来源更新时间
    msgsourceupdatetime = scrapy.Field()

