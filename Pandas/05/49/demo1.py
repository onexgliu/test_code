import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style('darkgrid')
# 读取数据集iris
df = pd.read_csv('iris.csv')
# 显示数据集
df.head()
# 绘制核密度图
# sns.kdeplot(df['sepal_width'], shade=True, bw=.5, color="orange")

# 绘制多个变量的核密度图
p1 = sns.kdeplot(df['sepal_width'], shade=True, color="r")
p1 = sns.kdeplot(df['sepal_length'], shade=True, color="b")
plt.show()
# 边际核密度图
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='kde', space=0)
plt.show()
