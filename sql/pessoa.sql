drop database curso;
create database curso;
use curso;

create table pessoas (
	id int not null auto_increment,
    nome varchar(30) not null,
    nascimento date,
    sexo enum('M', 'F'),
    peso decimal(5, 2),
    altura decimal(3,2),
    nacionalidade varchar(20) default 'Brasil',
    primary key (id)
    ) default charset = utf8;

insert into pessoas
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
values
(DEFAULT, 'Creuza', '1920-12-30', 'F', '50.2', '1.65', DEFAULT);

insert into pessoas
values
(DEFAULT, 'Adalgiza', '1930-11-2', 'F', '63.2', '1.75', 'Irlanda');

insert into pessoas
values
(DEFAULT, 'Cláudio', '1975-4-22', 'M', '99.0', '2.15', 'Brasil'),
(DEFAULT, 'Pedro', '1999-12-3', 'M', '87', '2', DEFAULT),
(DEFAULT, 'Janaina', '1987-11-12', 'F', '75.4', '1.66', 'EUA');

select * from pessoas;

# ------------------------------------------------------------------------

#alter table pessoas
#rename to gafanhotos;


alter table pessoas
add column profissao varchar(10) after nome;

/* alter table pessoas
change column profissao prof varchar(20) not null default '';

alter table pessoas
modify column profissao varchar(20) not null default ''; */


alter table pessoas
add codigo int first;

#alter table pessoas
#drop column profissao;


create table if not exists cursos (
    nome varchar(30) not null unique,
    descricao text,
    carga int unsigned,
    totaulas int,
    ano year default '2023'
    ) default charset = utf8;

alter table cursos 
add column idcurso int first;

alter table cursos
add primary key (idcurso);

desc cursos;

#drop table cursos

# ------------------------------------------------------------------------

insert into cursos values
('1', 'HTML4', 'Curso de HTML5', '40', '37', '2014'),
 ('2','Algoritimos','Logica de Programação','20','8','2014'),
 ('3','Photoshop','Aulas de Photoshop CC','9','20','2014'),
 ('4','PGP','PHP para Iniciantes','33','40','2010'),
 ('5','Jarva','Intro ao Java','22','10','2000'),
 ('6','MySQL','Curso MySQL','21','15','2016'),
 ('7','World','Word Completo','40','30','2018'),
 ('8','Sapateado','Dança Rítimica','14','30','2018'),
 ('9','Cozinha Árabe','Aprenda a fazer Kibe','40','30','2018'),
 ('10','YouTuber','Gerar Polêmicas e Ganhar Inscritos','5','2','2010');
 
 update cursos
 set nome = 'HTML5'
 where idcurso = '1';

update cursos
set nome = 'PHP', ano = '2015'
where idcurso = '4';

update cursos
set carga = '0', ano = '2010'
where ano = '2050'
limit 1;

delete from cursos
where idcurso = '8';

delete from cursos
where ano = '2050'
limit 2;

 select * from cursos;
 
 truncate table cursos;
 
 # -------------------------------------------------------------------------



