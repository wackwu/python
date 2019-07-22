# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2019年6月24日 20:40
# Target:我很喜欢看电影，我回忆了一下，这两年我觉得还不错的国产电影。
#        让其他人只要输入演员名，就打印出：××出演了电影××。


movies = {
'妖猫传':['黄轩','染谷将太'],
'无问西东':['章子怡','王力宏','祖峰'],
'超时空同居':['雷佳音','佟丽娅'],
}

actor = input('你想查询哪个演员？')
for  movie in movies:  # 用 for 遍历字典
    actors = movies[movie]  # 读取各个字典的主演表
    if actor in actors:
        print(actor + '出演了电影' + movie)