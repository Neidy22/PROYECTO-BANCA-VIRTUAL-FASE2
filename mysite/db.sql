create database django;
use django;
create table clienteIndividual(
	codigo int ,
    cui bigint,
    nit int,
    primary key (codigo,cui,nit),
    nombre varchar(100),
    nacimiento date,
    email varchar(150),
    usuario varchar(100),
    contrasenia varchar(100),
    telefono bigint
);

select * from clienteIndividual