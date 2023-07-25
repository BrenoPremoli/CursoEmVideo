select * from cursos
order by nome desc;

select * from cursos
where ano = '2016'
order by nome;

select nome, carga from cursos
where ano = '2016'
order by nome;

select nome, carga, ano from cursos
order by nome;

select ano, nome, carga from cursos
order by ano, nome;

select ano, nome, carga from cursos
order by ano, nome;

select nome, descricao, ano from cursos
where ano <= '2015'
order by ano, nome;

select nome, descricao, ano from cursos
where ano >= '2016'
order by ano, nome;

select nome, descricao, ano from cursos
where ano <> '2016'
order by ano, nome;

select nome, ano from cursos
where ano between 2014 and 2016
order by ano desc;

select nome, descricao, ano from cursos
where ano in (2014, 2016, 2020)
order by ano;

select nome, carga, totaulas from cursos
where carga > 35 and totaulas < 30
order by nome;

select nome, carga, totaulas from cursos
where carga > 35 or totaulas < 30
order by nome;

select * from cursos
where nome like 'p%'; #Começa com P

select * from cursos
where nome like '%a'; #Finaliza com A

select * from cursos
where nome like '%a%'; #Finaliza, começa e tem A no meio

select * from cursos
where nome not like '%a%'; #não tem A

select * from cursos
where nome like 'ph%p';

select * from cursos
where nome like 'ph%p%';

select * from cursos
where nome like 'ph%p_'; # '_' - termina com algo no final

select * from cursos
where nome like 'p_p%';

select * from cursos
where nome like 'p__t%';

select * from gafanhotos
where nome like '%silva%';

select * from gafanhotos
where nome like '%silva';

select * from gafanhotos
where nome like 'silva%';

select distinct nacionalidade from gafanhotos
order by nacionalidade;

select distinct carga from cursos
order by carga;

select count(*) from cursos;

select count(carga) from cursos
where carga > 40;

select max(carga) from cursos;

select max(totaulas) from cursos where ano = '2016';

select min(carga) from cursos;

select nome, min(totaulas) from cursos 
where ano = '2016';

select sum(totaulas) from cursos
where ano = '2016';

select avg(totaulas) from cursos
where ano = '2016';

#1
select nome, sexo from gafanhotos
where sexo = 'F';

#2
select id, nome, nascimento from gafanhotos
where nascimento between '2000/1/1' and '2015/12/31'
order by nascimento;

#3
select nome, sexo, profissao from gafanhotos
where sexo = 'M' and profissao = 'Programador';

#4
select * from gafanhotos
where nacionalidade = 'Brasil' and nome like 'J%' and sexo = 'F';

#5
select nome, nacionalidade, peso from gafanhotos
where sexo = 'M' and nome like '%Silva%' and peso < '100';

#6
select max(altura) from gafanhotos
where sexo = 'M' and nacionalidade = 'Brasil';

#7
select avg(peso) from gafanhotos;

#8
select min(peso) from gafanhotos
where nascimento between '1990/1/1' and '2000/12/31' 
and sexo = 'F' and nacionalidade != 'Brasil';

#9
select * from gafanhotos
where sexo = 'F' and altura > '1.90';

select distinct totaulas from cursos
order by totaulas;

select totaulas, count(*) from cursos
group by totaulas
order by totaulas;

select carga, count(*) from cursos 
where totaulas = 30
group by carga;

select carga, nome from cursos 
where totaulas = 30;

select ano, count(*) from cursos
where totaulas > 30
group by ano
having ano > 2013
order by count(*) desc;

select avg(carga) from cursos;

select carga, count(*) from cursos 
where ano > 2015
group by carga
having carga > (select avg(carga) from cursos);

#1
select profissao, count(*) from gafanhotos
group by profissao;

#2
select sexo, count(*) from gafanhotos
where nascimento > '2005/1/1'
group by sexo;

#3
select nacionalidade, count(*) from gafanhotos
where nacionalidade != 'Brasil'
group by nacionalidade
having count(nacionalidade) > 3;

#4
select avg(altura) from gafanhotos;

select altura, count(*) from gafanhotos
where peso > '100'
group by altura
having altura > (select avg(altura) from gafanhotos);







