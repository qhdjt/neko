
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 01 title设置
plt.title("title")#括号当中输入标题的名称
plt.show()

# 如果title是中文，matplotlib会乱码，这时需要加上下面这段代码：
plt.rcParams['font.sans-serif']=['SimHei']
# 02 Figure对象
# 在matplotlib中，整个图像为一个Figure对象。在Figure对象中可以包含一个或者多个Axes对象。每个Axes(ax)对象都是一个拥有自己坐标系统的绘图区域。
plt.figure(figsize=(6, 3))
plt.plot(6, 3)
plt.plot(3, 3 * 2)
plt.show()

# 03 坐标轴及标签
plt.xlim(0,6) #x轴坐标轴
plt.ylim((0, 3))#y轴坐标轴
plt.xlabel('X')#x轴标签
plt.ylabel('Y')#y轴标签
plt.show()

# 如果需要将数字设为负数，也可能出现乱码的情况，这时候可以加下面的代码：
plt.rcParams['axes.unicode_minus']=False


# 04 设置label和legend

# 设置 label 和 legend 的目的就是为了区分出每个数据对应的图形名称,legend的loc参数用于设置图例位置。

plt.plot(2, 3, label="123")#第一个label
plt.plot(2, 3* 2, label="456")#第二个label
plt.legend(loc='best')#图列位置，可选best，center等
plt.show()



# 05 添加注释

# 有时候我们需要对特定的点进行标注，我们可以使用 plt.annotate 函数来实现:

# s: 注释信息内容
# xy:箭头点所在的坐标位置
# xytext:注释内容的坐标位置
# arrowprops：设置指向箭头的参数

x=np.linspace(0,10,200)#从0到10之间等距产生200个值
y=np.sin(x)
plt.plot(x,y,linestyle=':',color='b')
plt.annotate(s='标记点',xy=(3,np.sin(3)),xytext=(4,-0.5),weight='bold',color='b',arrowprops=dict(arrowstyle='-|>',color='k'))
plt.show()

# 05 使用子图

# 如果需要将多张子图展示在一起，可以使用 subplot() 实现。即在调用 plot()函数之前需要先调用 subplot() 函数。该函数的第一个参数代表子图的总行数，第二个参数代表子图的总列数，第三个参数代表活跃区域。

ax1 = plt.subplot(2, 2, 1)
plt.plot(x,np.sin(x), 'k')

ax2 = plt.subplot(2, 2, 2, sharey=ax1) # 与 ax1 共享y轴
plt.plot(x, np.cos(x), 'g')

ax3 = plt.subplot(2, 2, 3)
plt.plot(x,x, 'r')

ax4 = plt.subplot(2, 2, 4, sharey=ax3) # 与 ax3 共享y轴
plt.plot(x, 2*x, 'y')



# - matplotlib 绘图 -

# matplotlib画图可以总结为3个步骤：获取数据——画出基本图形——设置细节。获取的数据一般包括横坐标和纵坐标的数据，这个数据可以是读取的，也可以自己生成，本文为了方便演示，使用numpy和pandas生成随机数。

# matplotlib所提供的图形非常丰富，除了基本的柱状图、饼图、散点图等，还提供了极坐标图、3D图等高级图形，并且你可以自由选择和组合。每个图形函数下都有许多参数可设置，matplotlib提供的不仅仅是图形，还有更为精细的图像表达，你可以通过细节的设置来丰富你的可视化。



# 01 bar

# 柱状图

# 生成一个单系列的柱状图比较简单，只要确定x轴及y轴的数据，利用bar（）函数就能生成：

x = np.arange(10)
y = np.random.randint(0,20,10)
plt.bar(x, y)
plt.show()

# 除了单系列柱状图，matplotlib还提供了其它类型的柱状图，如多系列柱状图，堆叠图，水平向的条纹图等。plt.plot()适用于基本图表的绘制，kind可选类型有线形图、柱状图、密度图、堆叠图、面积图等，以横纵坐标两个维度为主。grid是显示网格，colormap是颜色展示，括号中可填颜色参数，如不填则会展示默认颜色。

# 多系列柱状图
df = pd.DataFrame(np.random.rand(10, 3), columns = ['a', 'b', 'c'])
df.plot(kind = 'bar', grid = True, colormap = 'summer_r')

# 想要实现堆叠效果，一定要加上stacked=true，否则输出图形就是一般的柱状图。

# 多系列堆叠图
df.plot(kind = 'bar',  grid = True, colormap = 'Blues_r', stacked = True)

# 水平向的条形图调用的是barh（）:

# 水平向
df.plot.barh( grid = True, colormap = 'BuGn_r')
# 与垂直柱状图一样，如果想要柱状图实现堆叠效果，则加上：stacked=true

# 02 scatter
# 散点图
# 绘制散点图，主要用到plt.scatter（）这个函数。
# x,y是必填参数；
# c(颜色：b--blue, c--cyan,g--green,k--black,m--magenta,r--red,w--white,y--yellow)；
# s：控制点的大小，默认为20)；
# marker：指定散点图点的形状，默认为圆形；
# alpha：指定对象的透明度；


# 绘制简单的散点图：

x = np.random.rand(10)
y = np.random.rand(10)
plt.scatter(x,y)
plt.show()

# 进行简单的一些参数设置：
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
s = (30 * np.random.rand(50))**2
plt.scatter(x, y,s, c=colors, alpha=0.5)
plt.show()

# 散点矩阵图scatter_matrix，diagonal = ''为每个指标的频率图，有kde及hist两个参数可选；range_padding 是图像在x轴，y轴原点附近的留白，值越大，图像离坐标原点的距离越大。

df = pd.DataFrame(np.random.randn(100, 4), columns = list('abcd'))
pd.scatter_matrix(df, figsize = (8,6),marker = 'o',diagonal = 'kde',alpha = 0.4,range_padding = 0.05)

# 03 pie
# 饼图
# matplotlib中饼图的实现用的是pie（）函数，必须输入的参数是饼图每个部分的值。
x = np.random.randint(1, 10, 3)
plt.pie(x)
plt.show()

# 部分参数解释:

# 使用labels为饼图加标签；

# autopct 控制饼图内百分比设置

# '%1.1f'指小数点前后位数(没有用空格补齐)，

# shadow是在饼图下画一个阴影，False即不画

sizes = [2,5,12]
labels = ['娱乐','育儿','饮食']
plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False,startangle=100)
plt.show()

# 04 直方图hist

# 直方图绘制为hist（）函数，参数如下：

# data:必选参数，绘图数据

# bins:直方图的长条形数目，可选项，默认为10

# normed:是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率。

# facecolor:长条形的颜色

# edgecolor:长条形边框的颜色

# alpha:透明度

s = pd.Series(np.random.randn(1000))
s.hist(bins = 20,histtype = 'bar',align = 'mid',orientation = 'vertical',alpha = 0.5,normed = True)

# 密度图，加上：

s.plot(kind = 'kde', style = 'k--')

# 柱状图能够实现堆叠，直方图也能实现堆叠,重点语句同样是stacked = True

df = pd.DataFrame({'a':np.random.randn(500) + 1, 'b':np.random.randn(500),
'c':np.random.randn(500) - 1, 'd':np.random.randn(500)},
columns = list('abcd'))
df.plot.hist(stacked = True,bins = 10,colormap = 'Blues_r',alpha = 0.5,grid = True)



# 05 polar

# 极坐标图
#
# matplotlib的pyplot子库提供了绘制极坐标图的方法。在调用subplot()创建子图时通过设置projection='polar',便可创建一个极坐标子图，然后调用plot()在极坐标子图中绘图。

ax1 = plt.subplot(121, projection='polar')

# 部分参数意义：

# theta：角度数据
# radii ：极径数据
# theta_direction方法用于设置极坐标的正方向
# theta_zero_location方法用于设置极坐标0°位置，0°可设置在八个位置，分别为N, NW, W, SW, S, SE, E, NE
# thetagrids方法用于设置极坐标角度网格线显示
# theta_offset方法用于设置角度偏离

# 极区图：

N = 20
theta = np.linspace(0, 2 * np.pi, N, endpoint = False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection = 'polar')
bars = ax.bar(theta, radii, width = width, bottom = 0.0)

# 极散点图：

theta = np.arange(0,2*np.pi, np.pi/4) # 数据角度
r = np.arange(1,9,1) #数据极径
area = 100*np.arange(1,9,1) # 数据散点面积
colors = theta
ax2 = plt.subplot(111,projection='polar')
ax2.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha =0.75)

# 06 boxplot
# 箱型图

# 绘制箱线图，用plt.boxplot()这个函数。箱型图是利用数据中的五个统计量：最小值、第一四分位数、中位数、第三四分位数与最大值来描述数据的一种方法。它也可以粗略地看出数据是否具有有对称性，分布的分散程度等信息，特别可以用于对几个样本的比较。


# 箱线图各部分含义
# 部分参数：sym：异常值的形状 ；whis：用于调节上下垂直线的长度

# 生成单个箱型图：

np.random.seed(100)#生成随机数
data=np.random.normal(size=1000,loc=0,scale=1)
plt.boxplot(data,sym='o',whis=1.5)
plt.show()

# 多个箱型图：

np.random.seed(100)#生成随机数
data=np.random.normal(size=(1000,4),loc=0,scale=1) #1000个值得4维数组
lables = ['A','B','C','D']
plt.boxplot(data,labels=lables)
plt.show()

# 箱型图也可以是横向的，加上vert=False即可：


# 07 heatmap
#
# 热图

# 热图是数据分析的常用方法，通过色差、亮度来展示数据的差异、易于理解。matplotlib中生成热图是调用的函数imshow（）。
#
X = [[1,2],[3,4],[5,6]]
plt.imshow(X)
plt.show()
# 增加颜色类标的代码是plt.colorbar()：


# -可视化控制-

# 前面我们用matplotlib绘制了许多不同类型的图像，对于基本的数据分析已经完全掌握。但在一些细节的调节、颜色、美观度上我们没有做过多强调，matplotlib所提供的不仅仅是图形的基本绘制，它也提供了让图像展示更精细的工具。

# 颜色表示

# 八种内件颜色缩写：
# b:blue
# g:green
# r:red
# c:cyan
# m:magenta
# y:yellow
# k:black
# w:white

# 先用numpy生成四条线，再对四条线的颜色进行设置：

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
y=np.arange(1,5)
# 01 简单颜色展示

plt.plot(y,color='b')


# 02 灰色度

plt.plot(y+1,color='0.5') #灰色 程度为0.5


# 03 十六进制颜色表示

# 十六进制颜色代码可通过百度颜色代码（对照表查找）

plt.plot(y+2,color='#FFEC8B')


# 04 RGB 表示

# 此时注意要将R，G，B每个值除以255，使其属于0~1之间，如下为红色:

plt.plot(y+3,color=(1,0,0))
# 效果图：


# 点、线样式

# 01 四种线型

plt.plot(y,'-') #实线
plt.plot(y+1,'--')#虚线
plt.plot(y+2,'-.')#点划线
plt.plot(y+3,':')#点线

# 02 点样式

plt.plot(y,'o')
plt.plot(y+1,'D')
plt.plot(y+2,'^')
plt.plot(y+3,'p')

# 指定marker时，会画出线段：

plt.plot(y,marker='o')
plt.plot(y+1,marker='D')

# 03 样式字符串

# 将颜色，点型，线型写成一个字符串，如:gx：，mo--等
#
plt.plot(y,'gx:')
plt.plot(y+1,'mo--')
plt.plot(y+2,'bp-')

# 保存图片

plt.savefig() # 保存
# 关于 matplotlib，基本的图形绘制到这里就差不多了，虽然只是最常规的图形，但是足够让你开始尝试探索数据，快速绘图并获得分析结果。
# 探索性数据分析的路很长，但开始足够简单，去创造属于你的图形吧。