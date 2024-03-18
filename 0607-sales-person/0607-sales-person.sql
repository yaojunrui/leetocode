-- # Write your MySQL query statement below
-- select s.name from salesPerson s, company c, orders o
-- where s.sales_id = o.sales_id and c.com_id = o.com_id and c.name <> "RED"

select s.name from salesperson s left join orders o
on s.sales_id = o.sales_id  left join company c
on  c.com_id = o.com_id
group by s.sales_id
having sum(ifnull(c.name="RED", 0)) = 0;