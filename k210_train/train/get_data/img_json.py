# coding:utf-8
import requests
import json
import os

def download_url(url="https://xx.com/1.jpg", pre="" ,out_dir="./ts_save/"):
    img_name = url.split('/')[-1]
    ex = os.path.splitext(img_name)[1] # .jpg
    n = os.path.splitext(img_name)[0] # xx
    new_name = (str(pre) +n+ ex)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    save_dir = os.path.join(out_dir , new_name )
    print("save_dir:",save_dir)
    try:
        pic = requests.get(url, timeout=10)
        fp = open(save_dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('[图片无法下载]',url)


if __name__ == "__main__":
    url ="https://i1.wp.com/i.stack.imgur.com/4NEoL.png"
    out_dir = "/Users/liampro/Downloads/pro/git/ai-test/k210/k210_train/ts_save/1"
    download_url(url= url , pre='a_',out_dir=out_dir)


'''
query = '王祖贤'

def download(src, id):
    dir = './ts_data/aa/' + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载',src)
'''

'''例子： for 循环 请求全部的 url '''
''' 
for i in range(0, 22471, 20):
    url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i)
    html = requests.get(url).text  # 得到返回结果
    response = json.loads(html, encoding='utf-8')  # 将 JSON 格式转换成 Python 对象
    for image in response['images']:
        print(image['src'])  # 查看当前下载的图片网址
        download(image['src'], image['id'])  # 下载一张图片

'''
'''
{"images":
       [{"src": …, "author": …, "url":…, "id": …, "title": …, "width":…, "height":…},
    …
   {"src": …, "author": …, "url":…, "id": …, "title": …, "width":…, "height":…}],
 "total":22471,"limit":20,"more":true}
'''

''' 例子 box 
https://boxapi.makeblock.com/api/v2/courses?courseType=0

code: 0
get_data: [{courseID: 1128, name: "亲子准备课",…}, {courseID: 1129, name: "声控灯",…}, {courseID: 1130, name: "翻转灯",…},…]
[0 … 99]
0: {courseID: 1128, name: "亲子准备课",…}
courseID: 1128
ideURL: "https://res-cn.makeblock.com/cbox/cms/92836290-daf8-11ea-982a-b31c235823ea.mblock"
image: "https://res-cn.makeblock.com/cbox/cms/86f4f370-a0bb-11ea-bfd6-911df0ffb9ad.jpg"
'''
'''
for i in [1]:
    url = "https://boxapi.makeblock.com/api/v2/courses?courseType=0"
    html = requests.get(url).text  # 得到返回结果
    response = json.loads(html, encoding='utf-8')  # 将 JSON 格式转换成 Python 对象
    for image in response['get_data']:
        print(image['image'])  # 查看当前下载的图片网址
        download(image['image'], image['courseID'])  # 下载一张图片
'''

# test one
#url ='https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2883310817,3567497503&fm=26&gp=0.jpg'
#download(url,1)

