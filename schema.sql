drop table if exists users;
create table users(
 username text not null primary key,
 email text not null,
 name text not null
);