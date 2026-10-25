-- 1. 计算复购率
SELECT 
    COUNT(DISTINCT user_id) AS total_buyers, -- 总购买人数
    SUM(CASE WHEN buy_count > 1 THEN 1 ELSE 0 END) AS repeat_buyers, -- 复购人数
    ROUND(SUM(CASE WHEN buy_count > 1 THEN 1 ELSE 0 END) / COUNT(DISTINCT user_id), 4) AS repurchase_rate -- 复购率
FROM (
    SELECT user_id, COUNT(*) AS buy_count
    FROM ecommerce_project.ecommerce_data
    WHERE behavior = 'buy' -- 只看购买行为
    GROUP BY user_id
) AS user_buys;

-- 2. 计算次日留存率
WITH first_buy AS (
    -- 找出每个用户的首次购买日期
    SELECT user_id, MIN(DATE(time)) AS first_date
    FROM ecommerce_project.ecommerce_data
    WHERE behavior = 'buy'
    GROUP BY user_id
),
next_day_active AS (
    -- 找出首次购买后，第二天还有任何行为（浏览、加购、购买）的用户
    SELECT DISTINCT b.user_id
    FROM ecommerce_project.ecommerce_data b
    JOIN first_buy f ON b.user_id = f.user_id
    WHERE DATE(b.time) = DATE_ADD(f.first_date, INTERVAL 1 DAY)
)
-- 计算留存率
SELECT 
    COUNT(DISTINCT f.user_id) AS day0_buyers, -- 首购用户数
    COUNT(DISTINCT n.user_id) AS day1_active, -- 次日活跃用户数
    ROUND(COUNT(DISTINCT n.user_id) / COUNT(DISTINCT f.user_id), 4) AS retention_rate -- 次日留存率
FROM first_buy f
LEFT JOIN next_day_active n ON f.user_id = n.user_id;