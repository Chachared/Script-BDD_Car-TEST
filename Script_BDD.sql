Drop table engine cascade;
Drop table car cascade;
Drop table model cascade;
Drop table info cascade;

Create table engine (
  engLink VARCHAR (20) NOT NULL,
  engCode VARCHAR (20),
  engDesc VARCHAR (1000),
  engAspi VARCHAR (50),
  engAlim VARCHAR (20),
  engNameCyl VARCHAR (10),
  engValve INT,
  engDisp VARCHAR (10),
  engType VARCHAR (10),
  engKW INT,
  engCV INT,
  engCyl INT,  
  engNbCyl INT,
  PRIMARY KEY (engLink)
);

Create table car (
  C4Cid VARCHAR (20) NOT NULL,
  engLink VARCHAR (20) NOT NULL,
  modLink VARCHAR (20) NOT NULL,
  infoLink VARCHAR (20) NOT NULL,
  TDid VARCHAR (20),
  EBAYid INT,
  carFuel VARCHAR (50),
  carDesc VARCHAR (1000),
  carTrans VARCHAR (50),
  carTrim VARCHAR (50),
  carVersion VARCHAR (50),
  carPlat VARCHAR (20),
  carYFrom DATE,
  carYTo DATE,
  carYear DATE,
  PRIMARY KEY (C4Cid)
);

Create table model (
  modLink VARCHAR (20) NOT NULL,
  modMark VARCHAR (50),
  modName VARCHAR (100),
  modDoors VARCHAR (50),
  modChassis VARCHAR (50),
  modYFrom DATE,
  modYTo DATE,
  PRIMARY KEY (modId)
);

Create table info (
  infoLink VARCHAR (20) NOT NULL,
  infoDateAdd DATE,
  infoURL VARCHAR (100),
  infoUser VARCHAR (50),
  infoMethod VARCHAR (20),
  infoValid BOOLEAN DEFAULT FALSE,
  infoComment VARCHAR (1000),
  PRIMARY KEY (infoLink)
);

ALTER TABLE car
    ADD CONSTRAINT fk_engLink FOREIGN KEY (engLink) REFERENCES engine (engLink);

ALTER TABLE car
    ADD CONSTRAINT fk_modLink FOREIGN KEY (modLink) REFERENCES model (modLink);
	
ALTER TABLE car
    ADD CONSTRAINT fk_infoLink FOREIGN KEY (infoLink) REFERENCES info (infoLink);