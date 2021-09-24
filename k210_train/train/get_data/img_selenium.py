# coding:utf-8

"""
环境：Mac Python3
pip install -U selenium
下载chromedriver，放到项目路径下
（https://npm.taobao.org/mirrors/chromedriver/2.33/）
 https://sites.google.com/a/chromium.org/chromedriver/downloads

 问题：
 无法打开“chromedriver”，因为无法验证开发者。 仍然运行
 macOS无法验证“chromedriver”的开发者。您确定要打开它吗？  打开
"""

import requests
import json
import os
from lxml import etree
from selenium import webdriver
import time

query = '张柏芝'
downloadPath = './ts_data/img2'
chromedriver_url = '/Users/liampro/sdk/chrome/v89/chromedriver'
''' 下载图片 '''

driver = webdriver.Chrome(chromedriver_url)

def download(src, id):
    #dir = downloadPath + str(id) + '.jpg'
    #dir = os.path.join(downloadPath, os.path.basename(src)) #./ts_data/img2/p1394446025.33.webp
    old_name = os.path.basename(src)
    ex = os.path.splitext(old_name)[1] # .jpg
    name = (str(id) + ex)  # 123.jpg
    dir = os.path.join(downloadPath, name)
    #print(dir) #./ts_data/img2/张柏芝 Cecilia Cheung.webp
    if not os.path.exists(downloadPath):
        os.mkdir(downloadPath)
    if os.path.exists(dir):
        print('已存在:' + id)
        return
    try:
        pic = requests.get(src, timeout=20)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        # print 'error, %d 当前图片无法下载', %id
        print('图片无法下载:'+id)



def get_json_img():
    """ for 循环 请求全部的 url """
    for i in range(0, 22471, 20):
        url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i)
        # https://www.douban.com/j/search_photo?q=张柏芝&limit=20&start=20
        html = requests.get(url).text  # 得到返回结果
        print('html:' + html)
        response = json.loads(html, encoding='utf-8')  # 将 JSON 格式转换成 Python 对象
        for image in response['images']:
            print(image['src'])  # 查看当前下载的图片网址
            download(image['src'], image['id'])  # 下载一张图片


def get_xpath_img_by_page(url=''):
    # https://movie.douban.com/subject_search?search_text=张柏芝&cat=1002
    #url = 'https://movie.douban.com/subject_search?search_text=' + query + '&cat=1002'
    #driver = webdriver.Chrome(chromedriver_url)
    driver.get(url)
    html = etree.HTML(driver.page_source)
    # 使用xpath helper, ctrl+shit+x 选中元素，如果要匹配全部，则需要修改query 表达式
    src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
    title_xpath = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"

    srcs = html.xpath(src_xpath)
    titles = html.xpath(title_xpath)
    for src, title in zip(srcs, titles):
        print('\t'.join([str(src), str(title.text)]))
        #https://img2.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1394446025.33.webp	张柏芝 Cecilia Cheung
        download(src, title.text)
        time.sleep(0.005)

    #driver.close()

def multiple_page_by_xpath():
    for i in range(0, 61, 15):
        url = 'https://movie.douban.com/subject_search?search_text=' + query + '&cat=1002'+ '&start=' + str(i)
        print('分页：start:%d',i)
        time.sleep(0.005)
        get_xpath_img_by_page(url)
    time.sleep(0.5) # # Sleep for x *1000 milliseconds
    driver.close()



#test one
#download('https://img2.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1394446025.33.webp','张柏芝 Cecilia Cheung')

#test more
#url = 'https://movie.douban.com/subject_search?search_text=' + query + '&cat=1002'
#get_xpath_img_by_page(url)
#driver.close()

# multiple
multiple_page_by_xpath()






""" data:
<div class="item-root">
    <a href="https://movie.douban.com/celebrity/1003495/" data-moreurl="" class="cover-link">
        <img src="https://img9.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1394446025.33.webp" alt="张柏芝 Cecilia Cheung" class="cover">
    </a>
    <div class="detail">
        <div class="title"><a href="https://movie.douban.com/celebrity/1003495/" data-moreurl="" class="title-text">张柏芝 Cecilia Cheung</a></div>
        <div class="meta abstract" style="overflow: hidden;"><div class="meta abstract" style="line-height: 16.8px;">11519 人收藏</div>
    </div>
    <div class="meta abstract_2" style="overflow: hidden;"><div class="meta abstract_2" style="line-height: 18px;">演员 / 配音 / 制片人 / 1980-05-24 / 喜剧之王 / 新喜剧之王 / 少林足球</div></div></div>
</div>

"""