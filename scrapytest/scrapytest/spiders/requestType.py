# coding:utf-8
import random
import requests
from bs4 import BeautifulSoup


'''请求处理类'''

#动态获取浏览器User-Agent
def get_user_agent():
    user_agent_list = []
    f = open('D:\\learnPython\\scrapytest\\scrapytest\\spiders\\user_agent.txt', 'r')
    for date_line in f:
        user_agent_list.append(date_line.replace('\n', ''))
    user_agent = random.choice(user_agent_list)
    return user_agent

#封装headers
def get_headers():
    user_agent = get_user_agent()
    headers = {
        "Host": "dailianmeng.com",
        "Connection": "keep-alive",
        "User-Agent": user_agent,
        "referer":""

    }
    return headers

