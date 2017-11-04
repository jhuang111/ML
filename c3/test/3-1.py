#-*- coding:utf-8 -*-
from matplotlib.font_manager import *
import pandas as pd
import matplotlib.pyplot as plt
catering_sale='../data/catering_sale.xls'
data=pd.read_excel(catering_sale,index_col=u'日期')
myfont=FontProperties(fname='/home/hj/.fonts/wps-office/FZWBK.TTF')
plt.rcParams['axes.unicode_minus']=False
plt.figure()
p=data.boxplot()
#plt.title(u'销量',fontproperties=myfont)
x=p['fliers'][0].get_xdata()
y=p['fliers'][0].get_ydata()
for i in range(len(x)):
    print i;
    if i>0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.01-0.8/(y[i]-y[i-1]),y[i]))#防止同一行的数字重叠
    else:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.01,y[i]))
plt.show()
