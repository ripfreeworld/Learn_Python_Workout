postgres=# \connect wepython
You are now connected to database "wepython" as user "ripfreeworld".
wepython=# create table persons(name varchar(40) not null, id int primary key);
CREATE TABLE
wepython=# create table exercise(id int primary key, task varchar(100));
CREATE TABLE
wepython=# \dt
            List of relations
 Schema |   Name   | Type  |    Owner     
--------+----------+-------+--------------
 public | exercise | table | ripfreeworld
 public | persons  | table | ripfreeworld
(2 rows)

wepython=# create table whodidwhat(perid int, exid int, foreign key (perid) references persons(id), foreign key (exid) references exercise (id));
CREATE TABLE
wepython=# \dt
             List of relations
 Schema |    Name    | Type  |    Owner     
--------+------------+-------+--------------
 public | exercise   | table | ripfreeworld
 public | persons    | table | ripfreeworld
 public | whodidwhat | table | ripfreeworld
(3 rows)

wepython=# insert into persons (id, name) values (1, 'liuchenyang'), (2, 'duchangyu'), (3, 'lingxuebo');
INSERT 0 3
wepython=# insert into exercise (id, task) values (1, 'guess random integer');
INSERT 0 1
wepython=# insert into whodidwhat (perid, exid) values (1, 1);
INSERT 0 1
                                                  ^
wepython=# select * from persons natural join exercise;
 id |    name     |         task         
----+-------------+----------------------
  1 | liuchenyang | guess random integer
(1 row)

wepython=# 
