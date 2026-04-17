CREATE TABLE shops (
    id INT,
    shop_name VARCHAR(50),
    revenue INT
);

INSERT INTO shops VALUES
(1, 'Shop1', 600000),
(2, 'Shop1', 500000),
(3, 'Shop2', 300000);

SELECT shop_name, SUM(revenue) AS total_revenue
FROM shops
GROUP BY shop_name
HAVING SUM(revenue) > 1000000;
