#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.mlab import griddata
X=[];Y=[];Z=[]
for l in (open("data.txt",'r')):
    X.append(float(l.split()[0]))
    Y.append(float(l.split()[1]))
    Z.append(float(l.split()[2]))
#由于原数据各点比较离散，需要进行插值处理。分别在x的最小值与最大值之间、y的最小值与最大值之间插入1000个点，对z进行线性插值
x=np.linspace(min(X),max(Y),1000)
y=np.linspace(min(Y),max(Y),1000)
z=griddata(X,Y,Z,x,y, interp='linear')
plt.contour(x,y,z,10)#调用contour绘制等高线，条数为10条
cs= plt.contour(x,y,z,10,colors='k');
plt.clabel(cs, fontsize=9,fmt='%d', inline=1,colors='k')
#调用contourf绘制二维地形图
plt.contourf(x,y,z,15)
cbar=plt.colorbar()#调用colorbar绘制彩条
#设置各种标签
#显示中文时需要用u'中文',但是由于matplotlib.pyplot在显示时无法找到合适的字体，会显示乱码（我的显示为方框），因此需要设定字体
cbar.set_label(u'高程',fontproperties='SimHei')
plt.title(u'某地区地形图',fontproperties='SimHei');plt.xlabel('x');plt.ylabel('y')
plt.savefig('地形图.png',)
plt.show()




