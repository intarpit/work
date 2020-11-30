"""
Below are the some SQL queries written for a project.
"""
1. select distinct(title) from movies where year = '2008';

2. select birth from people where name = 'Emma Stone';

3. select distinct(title) from movies where year >= '2018' order by title;

4. select count(movie_id) from ratings where rating = '10.0';

5. select title, year from movies where title like 'Harry Potter%' order by year;

6. select avg(r.rating) from ratings as r
join movies as m on r.movie_id = m.id
where m.year = '2012';

7. select m.title, r.rating from movies as m
join ratings as r on m.id = r.movie_id
where m.year = '2010'
order by r.rating desc;

8. select name from people as p
join stars as s on p.id = s.person_id
join movies as m on m.id = s.movie_id
where title = 'Toy Story';

9. select distinct(p.name) from people as p
join stars as s on s.person_id = p.id
join movies as m on m.id = s.movie_id
where m.year = '2004'
order by p.birth;

10. select distinct(p.name) from people as p
join directors as d on d.person_id = p.id
join ratings as r on r.movie_id = d.movie_id
where r.rating >= '9.0';

11. select m.title from movies as m
join ratings as r on r.movie_id = m.id
join stars as s on s.movie_id = m.id
join people as p on p.id = s.person_id
where p.name = 'Chadwick Boseman'
order by rating desc
limit 5;

12. select m.title from movies as m
join stars as s on s.movie_id = m.id
join people as p on p.id = s.person_id
where (p.name = 'Johnny Depp') and
(p.name = 'Helena Bonham Carter');

13. select distinct(p.name) from people as p
join stars as s on s.person_id = p.id
join movies as m on m.id = s.movie_id
where title like
(select distinct(m.title) from movies as m
join stars as s on s.person_id = p.id
join people as p on p.id = s.person_id
where p.name = 'Kevin Bacon' and
p.birth = '1958'
);