# 电商用户留存与复购分析（个人项目）

## 📌 项目背景
基于 10,000 条模拟电商用户行为数据（含浏览、加购、购买），独立完成从数据生成、入库到指标计算的完整数据分析闭环。

## 🛠 技术栈
*   **编程语言**：Python (Pandas)
*   **数据库**：MySQL (SQLAlchemy, CTE, 窗口函数)
*   **数据可视化**：Matplotlib

## ⚙️ 项目流程
1.  **数据源与入库**：使用 Python 生成 1 万条具有业务特征的模拟数据，并保存为 CSV，通过 SQLAlchemy 极速导入本地 MySQL 数据库。
2.  **核心指标计算**：编写 SQL 脚本，使用 `GROUP BY` 和 `CASE WHEN` 计算用户**复购率**；使用 `CTE (WITH)` 计算**次日留存率**。
3.  **数据可视化**：通过 Python 连接 MySQL 提取聚合结果，使用 Matplotlib 绘制用户复购分布饼图。

## 📊 核心洞察
*   复购用户占比达到 **21.78**%。
*   建议针对仅购买一次的用户，在首购后 24 小时内进行触达干预，以提升次日留存和复购转化。

## 📁 文件说明
*   `import_all.py`：数据生成及导入脚本
*   `metrics.sql`：核心指标计算 SQL 代码
*   `03_visualization.py`：数据可视化脚本
*   `user_repurchase_chart.png`：最终生成的图表
*   `ecommerce_data.csv`：项目使用的电商行为模拟源数据
