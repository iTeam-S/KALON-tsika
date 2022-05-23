#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: Type
#------------------------------------------------------------

CREATE TABLE Type(
        id_type Int  Auto_increment  NOT NULL ,
        type    Varchar (100) NOT NULL
	,CONSTRAINT Type_PK PRIMARY KEY (id_type)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Artiste
#------------------------------------------------------------

CREATE TABLE Artiste(
        id_artiste  Int  Auto_increment  NOT NULL ,
        nom_artiste Varchar (100) NOT NULL
	,CONSTRAINT Artiste_PK PRIMARY KEY (id_artiste)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Album
#------------------------------------------------------------

CREATE TABLE Album(
        id_album   Int  Auto_increment  NOT NULL ,
        nom_album  Varchar (50) NOT NULL ,
        photo      Varchar (50) NOT NULL ,
        id_artiste Int NOT NULL
	,CONSTRAINT Album_PK PRIMARY KEY (id_album)

	,CONSTRAINT Album_Artiste_FK FOREIGN KEY (id_artiste) REFERENCES Artiste(id_artiste)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Musique
#------------------------------------------------------------

CREATE TABLE Musique(
        id_chant         Int  Auto_increment  NOT NULL ,
        titre            Varchar (50) NOT NULL ,
        photo_couverture Varchar (250) NOT NULL ,
        id_album         Int NOT NULL ,
        id_artiste       Int NOT NULL
	,CONSTRAINT Musique_PK PRIMARY KEY (id_chant)

	,CONSTRAINT Musique_Album_FK FOREIGN KEY (id_album) REFERENCES Album(id_album)
	,CONSTRAINT Musique_Artiste0_FK FOREIGN KEY (id_artiste) REFERENCES Artiste(id_artiste)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Media
#------------------------------------------------------------

CREATE TABLE Media(
        id_media Int  Auto_increment  NOT NULL ,
        media    Varchar (100) NOT NULL ,
        id_chant Int NOT NULL ,
        id_type  Int NOT NULL
	,CONSTRAINT Media_PK PRIMARY KEY (id_media)

	,CONSTRAINT Media_Musique_FK FOREIGN KEY (id_chant) REFERENCES Musique(id_chant)
	,CONSTRAINT Media_Type0_FK FOREIGN KEY (id_type) REFERENCES Type(id_type)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Tournee
#------------------------------------------------------------

CREATE TABLE Tournee(
        id_tournee   Int  Auto_increment  NOT NULL ,
        date_tournee Date NOT NULL ,
        lieu         Varchar (250) NOT NULL ,
        image        Varchar (250) NOT NULL ,
        id_artiste   Int NOT NULL
	,CONSTRAINT Tournee_PK PRIMARY KEY (id_tournee)

	,CONSTRAINT Tournee_Artiste_FK FOREIGN KEY (id_artiste) REFERENCES Artiste(id_artiste)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Reservation
#------------------------------------------------------------

CREATE TABLE Reservation(
        id_reservation Int  Auto_increment  NOT NULL ,
        date_debut     Datetime NOT NULL ,
        date_fin       Datetime NOT NULL ,
        nbre_billet    Varchar (50) NOT NULL ,
        id_tournee     Int NOT NULL
	,CONSTRAINT Reservation_PK PRIMARY KEY (id_reservation)

	,CONSTRAINT Reservation_Tournee_FK FOREIGN KEY (id_tournee) REFERENCES Tournee(id_tournee)
)ENGINE=InnoDB;

