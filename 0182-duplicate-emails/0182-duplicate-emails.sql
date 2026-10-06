# Write your MySQL query statement below
select email from person
where email is not null
group by email
having count(*)>1;