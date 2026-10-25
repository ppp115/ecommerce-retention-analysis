import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# 1. 连接 MySQL 数据库
print("⏳ 正在连接数据库...")
engine = create_engine("mysql+pymysql://root:Pyl1216115@localhost:3306/ecommerce_project")

# 2. 用 SQL 把用户的购买行为统计出来
sql_query = """
    SELECT user_id, COUNT(*) as buy_count
    FROM ecommerce_data
    WHERE behavior = 'buy'
    GROUP BY user_id;
"""
df = pd.read_sql(sql_query, engine)

# 3. 数据处理：把用户按购买次数分为“仅购买1次”和“复购(2次及以上)”
df['user_type'] = df['buy_count'].apply(lambda x: '复购用户' if x > 1 else '单次购买用户')
type_counts = df['user_type'].value_counts()

# 4. 画图
plt.figure(figsize=(8, 5))
# 解决中文显示问题（如果你电脑没装中文字体，图表可能会显示方块，但图形是对的）
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False

# 画一个饼图
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#ff9999'])
plt.title('电商用户复购分布图')

# 保存图片到本地
plt.savefig('user_repurchase_chart.png')
print("🎉 成功！图表已保存为 user_repurchase_chart.png")

# 显示图表
plt.show()