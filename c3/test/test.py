#-*- coding: utf-8 -*-
import pandas as pd
catering_sale='../data/catering_sale.xls'
data=pd.read_excel(catering_sale,index_col=u'日期')
print data.describe()
