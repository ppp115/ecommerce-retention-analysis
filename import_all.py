import pandas as pd
from sqlalchemy import create_engine

# 1. 读取 CSV 文件（直接写死你 E 盘的绝对路径，绝不报错）
csv_path = r"E:\SQL\ecommerce_data.csv"
df = pd.read_csv(csv_path)
print(f"✅ 成功读取 CSV 文件，共 {len(df)} 行数据。")

# 2. 连接 MySQL（注意：密码是你截图里的那个，如果不确定请改成你自己的）
# 格式：mysql+pymysql://用户名:密码@localhost:3306/数据库名
engine = create_engine("mysql+pymysql://root:Pyl1216115@localhost:3306/ecommerce_project")
print("✅ 成功连接 MySQL 数据库。")

# 3. 导入数据到表 (replace 表示如果表里有数据就覆盖掉)
print("⏳ 正在极速导入数据...")
df.to_sql('ecommerce_data', con=engine, if_exists='replace', index=False)

print("🎉 数据全部导入完成！去 Workbench 查收吧！")