# Write your MySQL query statement below
select w2.Id from weather w1 join weather w2 on w2.temperature > w1.temperature
 and datediff(w1.recordDate, w2.recordDate) = -1
