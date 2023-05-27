import matplotlib.pyplot as plt
import numpy as np
plt.title("First 窗口")  # 括号当中输入标题的名称
# 如果title是中文，matplotlib会乱码，这时需要加上下面这段代码：
plt.rcParams['font.sans-serif']=['SimHei']
# 如果需要将数字设为负数，也可能出现乱码的情况，这时候可以加下面的代码：
plt.rcParams['axes.unicode_minus']=False

x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)

# 设置label和legend
# 设置 label 和 legend 的目的就是为了区分出每个数据对应的图形名称,legend的loc参数用于设置图例位置。
plt.plot(2, 3, label="123")#第一个label
plt.plot(2, 3* 2, label="456")#第二个label
plt.legend(loc='best')#图列位置，可选best，center等
plt.show()

