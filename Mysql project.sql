show databases;
show schemas;
SHOW ENGINE INNODB STATUS;
select* from salaries
limit 5;
select* from employees
limit 5;

select distinct(s.emp_no),s.salary,(select avg(s.salary) from salaries s) as avg_salary,
case 
when s.salary <= avg(s.salary) then 'parledu'
when s.salary <= avg(s.salary) then 'lyt'
end as cost_to_company
from salaries s
group by s.emp_no,s.salary;

select* from employees
limit 10;

select * from salaries;

select emp_no,salary, avg(salary) as avg_salary
from salaries
group by emp_no,salary
order by 1,2;

select a.emp_no,salary,avg_salary 
from (select emp_no,salary, avg(salary) over() as avg_salary
from salaries) a;

select emp_no,first_name,last_name,gender,hire_date
from employees
where exists (select * from dept_manager
				where employees.emp_no=dept_manager.emp_no);
 
                
select distinct(dm.emp_no),e.first_name,e.last_name,e.gender,e.hire_date
from dept_manager dm
join employees e on dm.emp_no=e.emp_no;

select substring('Total employees',7,9)as result,
count(emp_no) as emp_no,
count(distinct(first_name))as unique_firstnames
from employees;

select upper('hello')as uppercase_result,
lower('WORLD') as lowercase_result;

select length('hello world')as string_length;

select concat('sarigga',' ','chadava','ra',' ','errip*ka') as na_bratuku;

select count(distinct(salary)) as emp_salary
from salaries;

select distinct(salary),ifnull(emp_no,'NA')as emp_no
from salaries
order by salary desc
limit 1 offset 1;

select* from employees
limit 5;

select emp_no, coalesce(birth_date,first_name,last_name,gender,'No_Value') as result
from employees;

select emp_no, coalesce(salary,0)+10 as calculated_value
from salaries
order by calculated_value desc;

select emp_no,coalesce(birth_date,first_name,last_name,gender,0) as result
from employees
order by result desc;

select salary+10 
from salaries
order by salary desc;

select* from salaries
limit 10 offset 1;

select * from salaries
where salary in
(select salary from salaries
where salary between 63010 and 63011);

select salary from salaries
where salary between 63010 and 63011;

select * from salaries
where salary not in
(select salary from salaries
where salary between 30000 and 157000);

select*
from employees 
where exists
(select* from dept_manager
where employees.emp_no=dept_manager.emp_no);

select e.first_name,e.last_name
from employees e
join dept_manager t on
e.emp_no=t.emp_no;

select emp_no
from titles
where title like '%Senior Engineer%';

select * from salaries
limit 5;

select emp_no,salary, rank() over(partition by emp_no order by salary) as rankk
from salaries;

select emp_no, salary, dense_rank() over(partition by emp_no order by salary) as rankk
from salaries;

select emp_no,dept_no
from dept_manager
where exists
(select emp_no from salaries
where dept_manager.emp_no=salaries.emp_no
and salary>100000);

select * from emp_manager;

select emp_no,dept_no,manager_no
from emp_manager
where exists
(select emp_no
from salaries
where emp_manager.emp_no=salaries.emp_no
and salary>60000);

#find the list of emp_managers whose salaries are greater than 90000

select emp_no,dept_no
from emp_manager
where exists (select emp_no,salary from salaries
where emp_manager.emp_no=salaries.emp_no
group by emp_no);

select distinct e.emp_no,s.salary
from emp_manager e
inner join salaries s on
e.emp_no=s.emp_no;

select * from emp_manager e
inner join salaries s on
e.emp_no=s.emp_no
where salary>90000;

select * from emp_manager
where emp_no in
(select emp_no from salaries
where salary>90000);

select emp_no, ifnull(salary,'NA') as salary_status
from salaries;

select date_sub('2023-07-10',Interval 1 day) as next_day;

select date_add('2023-07-10', Interval 1 day) as next_day;

select datediff('2023-07-10','2023-06-10') as date_diff,
timestampdiff(Month,'2023-06-30','2023-07-30') as month_diff;

#select any employees that has a salray of 70000;

select *
from employees
where emp_no=any
(select emp_no from salaries
where salary=60000);

select count(*)
from emp_manager;
                