# Write your MySQL query statement below
select e2.name as Employee from Employee e1 join employee e2 on e1.id = e2.managerID
where e2.salary > e1.salary;
