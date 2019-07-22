# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年9月19日 16:00
# Target: 爬取糗事百科文字页面数据

# 导入需要使用的相关模块
import requests
from bs4 import BeautifulSoup

def download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}
    r = requests.get(url, headers=headers)
    return r.text

def get_content(html, page):
    output = """ 第{}页 作者:{} 性别:{} 年龄:{} 点赞:{} 评论:{}\n{}\n-----------------------------------\n"""
    soup = BeautifulSoup(html, 'html.parser')
    con = soup.find(id='content-left')
    con_list = con.find_all('div', class_="article")
    for i in con_list:
        # 获取作者名字
        author = i.find('h2').string
        # 获取内容
        content = i.find('div', class_='content').find('span').get_text()
        # 获取笑脸，评论数
        stats = i.find('div', class_='stats')
        # 获取笑脸数
        vote = stats.find('span', class_='stats-vote').find('i', class_='number').string
        # 获取评论数
        comment = stats.find('span', class_='stats-comments').find('i', class_='number').string
        # 获取作者、年龄、性别
        author_info = i.find('div', class_='articleGender')
        # 非匿名用户
        if author_info is not None:
            class_list = author_info['class']
            if "womenIcon" in class_list:
                gender = "女"
            elif "manIcon" in class_list:
                gender = "男"
            else:
                gender = ''
            # 获取年龄
            age = author_info.string
        else: # 匿名用户
            gender = ''
            age = ''

        save_text(output.format(page, author, gender, age, vote, comment, content))

def save_text(*arg):
    for i in arg:
        with open('/Users/wuxuhao/Desktop/Python/PaChong/QiuShiBaiKe/qiubai.text', 'a', encoding='utf-8') as f:
            f.write(i)

def main():
    # 点击下面链接，在页面下方看到共有13页，可以构造如下url，最好用Beautiful Soup找到页面底部有多少页
    for i in range(1, 14):
        url = 'https://www.qiushibaike.com/text/page/{}'.format(i)
        html = download_page(url)
        get_content(html, i)

if __name__ == '__main__':
    main()