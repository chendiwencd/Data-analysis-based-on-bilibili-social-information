import requests
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import selenium
import pandas as pd

# 获取当前时间并格式化文件名称
now = datetime.datetime.now()
current_time = now.strftime('%Y-%m-%d-%H-%M-%S')
filename2 = f'播放数据_{current_time}.txt'
# 获取html文件
url = 'https://www.bilibili.com/v/information/'

# 模拟请求
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
driver = webdriver.Chrome()
driver.get(url)

# 等待页面加载完成
driver.implicitly_wait(10)
# 模拟下滑页面的操作
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

# 获取页面源代码
html = driver.page_source
# 解析 HTML
soup = BeautifulSoup(html, 'html.parser')

# 获取视频列表
video_list2 = soup.find_all('span', class_='bili-video-card__stats--text')
# 将video_list写入文本
play_nums = []
comment_nums = []
for i in range(0, len(video_list2), 2):
    play_nums.append(video_list2[i].text)
    comment_nums.append(video_list2[i+1].text)

# 将数据写入文本文件
with open(filename, 'w', encoding='utf-8') as f:
    for play_num, comment_num in zip(play_nums, comment_nums):
        f.write(f'播放量：{play_num}，评论数：{comment_num}\n')





