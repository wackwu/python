# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年9月17日 15:00
# Target: 分析拉勾网数据

# 导入需要使用的相关模块
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from pylab import mpl
from scipy.misc import imread
import statsmodels.api as sm 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 由于我们显示的中文标签，绘图是需要定植中文
mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决'-'负号显示问题
# plt.style.use(‘ggplot’)使用R语言中的ggplot2配色作为绘图风格
plt.style.use('ggplot')

# 读取数据
filename = '/Users/wuxuhao/Desktop/Python/PaChong/LaGoujob/files/lagou_jobs.csv'
data = pd.read_csv(filename, encoding='utf-8', sep='\t')

# 查看数据维度
print(data.shape)

# 查看数据概述
print(data.describe())

# 查看数据类型
print(data.dtypes)

# 数据清洗，删除掉产品助理岗位
data.drop(data[data[u'职位名称'].str.contains(u'助理')].index, inplace=True)

# 查看数据清洗后的数据概况
print(data.describe())

# 统计无锡城市招聘产品经理的数量
citysum = data.groupby([u'城市']).size()
print(citysum)

# 由于CSV文件内的数据是字符串形式，先用正则表达式将字符串转化为列表，在取区间的均值
pattern = '\d+'
data[u'工作年限'] = data[u'工作经验'].str.findall(pattern)

avg_work_year = []
for i in data[u'工作年限']:
    # 如果工作年限为‘不限’或‘应届毕业生’，那么匹配值为空，工作年限为0
    if len(i) == 0:
        avg_work_year.append(0)
    # 如果匹配值为一个数据，那么返回该数值
    elif len(i) == 1:
        avg_work_year.append(int(''.join(i)))
    # 如果匹配为一个区间，那么取平均值
    else:
        num_list = [int(j) for j in i]
        avg_year = sum(num_list) / 2
        avg_work_year.append(avg_year)

data[u'经验'] = avg_work_year

# 将字符串转换为列表，再取区间的前25%，比较贴近现实
data[u'salary'] = data[u'工资'].str.findall(pattern)

avg_salary = []
for k in data['salary']:
    int_list = [int(n) for n in k]
    avg_wage = int_list[0] + (int_list[1] - int_list[0]) / 4
    avg_salary.append(avg_wage)

data[u'月工资'] = avg_salary

# 将清洗后的数据保存，以便检查
data.to_csv('/Users/wuxuhao/Desktop/Python/PaChong/LaGoujob/files/draft.csv', index=False, encoding='utf_8_sig')

# 描述统计
print(u'产品经理工资描述:\n{}'.format(data[u'月工资'].describe()))

# 绘制频率直方图并保存
plt.hist(data[u'月工资'], bins=12)
plt.xlabel(u'工资（千元）')
plt.ylabel(u'频数')
plt.title(u'工资直方图')
plt.savefig('/Users/wuxuhao/Desktop/Python/PaChong/LaGoujob/files/histogram.jpg')
plt.show()

# 绘制饼图并保存
count = data[u'城市'].value_counts()
plt.pie(count, labels=count.keys(), labeldistance=1.5, autopct='%2.1f%%')
plt.axis('equal') # 饼图为正圆形
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
plt.savefig('/Users/wuxuhao/Desktop/Python/PaChong/LaGoujob/files/pie_chart.jpg')
plt.show()

# 绘制词云，将职位福利中的字符串汇总
text = ''
for line in data[u'职位福利']:
    text += line
# 使用jieba模块将字符串分割为单词列表
cut_text = ' '.join(jieba.cut(text))
color_mask = imread('/Users/wuxuhao/Desktop/Python/PaChong/LaGoujob/files/wechat.jpg') # 设置背景图
cloud = WordCloud(
    font_path='Monaco Yahei.ttf',
    background_color='white',
    mask=color_mask,
    max_words=1000,
    max_font_size=100
)
word_cloud = cloud.generate(cut_text)
# 保存词云图片
word_cloud.to_file('/Users/wuxuhao/Desktop/Python/PaChong/LaGoujob/files/cloud.jpg')
plt.imshow(word_cloud)
plt.axis('off')
plt.show()

# 实证统计，将学历不限的职位要求认定为最低学历：大专
data[u'学历要求'] = data[u'学历要求'].replace(u'不限', u'大专')

# 学历分为大专\本科\硕士，将他们设定为虚拟变量
dummy_edu = pd.get_dummies(data[u'学历要求'], prefix=u'学历')
# 构建回归数组
df_with_dummy = pd.concat([data[u'月工资'], data[u'经验'], dummy_edu], axis=1)

# 建立多远回归模型
y = df_with_dummy[u'月工资']
x = df_with_dummy[[u'经验', u'学历_大专', u'学历_本科', u'学历_硕士']]
x = sm.add_constant(x)
model = sm.OLS(y, x)
results = model.fit()
print(u'回归方程的参数:\n{}\n',format(results.params))
print(u'回归结果:\n{}'.format(results.summay()))