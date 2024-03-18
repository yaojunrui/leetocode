# Write your MySQL query statement below
select max(unique_num) as num from (select num as unique_num from mynumbers
group by num
having count(num) = 1) as temp_table;


