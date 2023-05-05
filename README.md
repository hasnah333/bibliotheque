

*titre : system gestion bibliotheque

*les requêtes de mysql:

-base de donnée :gestionetudetlivre

-table utilisateur:CREATE TABLE users (id INT(6) UNSIGNED AUTO_INCREMENT  NOT NULL PRIMARY KEY ,username varchar(255)   UNIQUE , password varchar(255)  UNIQUE
-table livre: CREATE TABLE book(idbook varchar(25) not null,primary key(idbook),autor varchar(255)NOT NULL, title varchar(255)NOT NULL,anneParution varchar(255) NOT NULL,image varchar(255))


*les fonctionnalitées: adduser(): permet de l'utilisateur de crée un compt ,userSignIn(): permet au utilisateur de se connecter a son compte add(): permet a l'utilisateur d'ajouter un livre. delete(): permet a l'utilisateur de supprimer un livre. updatebook(): permet a l'utilisateur de modifier un livre serch(): permet a l'utilisateur de chercher un livre getimage(): permet a l'utilisateur d'affiher l'image d'un livre.
