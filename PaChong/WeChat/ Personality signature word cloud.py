#-*- coding：utf-8 -*-
#导入需要使用的相关模块
import itchat
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np
import PIL.Image as Image

#登陆方法，会弹出登陆二维码，用微信扫描登陆
itchat.auto_login()

#爬取自己好友相关信息，返回一个json文件
friends = itchat.get_friends(update=True)[0:]

#自定义好友个性签名的自定义词云图
myList = []
for i in friends:
    signature = i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1f\d.+")
    signature = rep.sub("",signature)
    myList.append(signature)

#拼接字符串
text = "".join(myList)

#jieba分词
wordlist_jieba = jieba.cut(text, cut_all = True)
word_space_split = " ".join(wordlist_jieba)

d = os.path.dirname(__file__)

coloring = np.array(Image.open(os.path.join(d, "wechat.jpg")))
my_wordcloud = WordCloud(background_color = "White", max_words = 2000, mask = coloring, max_font_size = 40,
                          random_state = 42, scale = 2, 
                          font_path = "/Users/sebastian/Library/Fonts/Arial Unicode.ttf")\
    .generate(word_space_split)
   
image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func = image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()