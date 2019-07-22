# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年9月17日 10:10
# Target: 爬取拉勾网数据

# 导入需要使用的相关模块
import requests
import math
import pandas as pd
import time


def john_get_json(url, num):
    ''' 从网页获取JSON格式数据，并使用POST模拟请求 '''
    Johnheaders = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'Referer':'https://www.lagou.com/jobs/list_%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86?labelWords=&fromSearch=true&suginput='
    }
    Johndata = {
        'first': 'true',
        'pn' : num,
        'kd' : '产品经理'
    }
    res = requests.post(url, headers = Johnheaders, data = Johndata)
    res.raise_for_status()
    res.encoding = 'utf-8'
    # 得到包含职位信息的字典
    page = res.json()
    # print page
    return page

def john_get_page_num(count):
    ''' 计算要抓娶的页数 '''
    # 每页15个职位
    res = math.ceil(count / 15)
    # 最多显示30页
    if res > 30:
        return 30
    else:
        return res

def john_get_page_info(jobs_list):
    ''' 对每页的职位信息进行解析，返回列表 '''
    page_info_list = []
    for i in jobs_list:
        job_info = []
        job_info.append(i['companyFullName'])
        job_info.append(i['companyShortName'])
        job_info.append(i['companySize'])
        job_info.append(i['financeStage'])
        job_info.append(i['city'])
        job_info.append(i['district'])
        job_info.append(i['positionName'])
        job_info.append(i['workYear'])
        job_info.append(i['education'])
        job_info.append(i['salary'])
        job_info.append(i['positionAdvantage'])
        page_info_list.append(job_info)
    return page_info_list

def main():
    #city=%E5%85%A8%E5%9B%BD 这是拉勾上城市定位【全国】，如果要获取某城市的数据，在这里修改
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    # 先设定页数为1，获取总的职位数，由于拉勾网显示2页的数据，所以我们抓取的数据总数为30条数据
    page_1 = john_get_json(url, 1)
    total_count = page_1['content']['positionResult']['totalCount']
    num = john_get_page_num(total_count)
    total_info = []
    time.sleep(20)
    print("职位总数:{}, 页数:{}".format(total_count, num))

    for n in range(1, num+1):
        # 读取JSON，获取数据
        page = john_get_json(url, n)
        jobs_list = page['content']['positionResult']['result']
        print(jobs_list)
        page_info = john_get_page_info(jobs_list)
        total_info += page_info
        print("已经抓取第{}页，职位总数:{}".format(n, len(total_info)))
        # 抓取完成，休息一会
        time.sleep(30)
    # dataframe输出数据
    df = pd.DataFrame(data = total_info, columns = ['公司全名', '公司简称', '公司规模', '融资阶段', '城市', '区域', '职位名称', '工作经验', '学历要求', '工资', '职位福利'])
    df.to_csv('/Users/wuxuhao/Desktop/Python/PaChong/LaGoujob/files/lagou_jobs.csv', index = False, encoding = 'utf-8')
    print("已经保存为csv文件。")

if __name__ == '__main__':
    main()