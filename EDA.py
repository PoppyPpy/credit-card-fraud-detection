# 生成EDA报告
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('archive/creditcard.csv')
profile = ProfileReport(df, title='信用卡欺诈数据EDA报告', explorative=True)
profile.to_file('creditcard_eda.html')  # 生成可交互的HTML报告