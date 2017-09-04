import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values,y_values,c=(1.0,0.5,0),edgecolor='none',s=40) #c为颜色值
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40) #颜色渐变
#设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis="both", which='major', labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1000000])

# 自动保存图表
plt.savefig('squares_plot.png', bbox_inches='tight')

# 显示
plt.show()