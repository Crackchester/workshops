DROP TABLE IF EXISTS ctf_workshop_dev.Users;

CREATE TABLE ctf_workshop_dev.Users (
  `username` varchar(245) NOT NULL,
  `password` varchar(45) NOT NULL,
  `cool` boolean,
  PRIMARY KEY (`username`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO ctf_workshop_dev.Users (username, password, cool)
VALUES
	('DaFlag','CTF_FLAG{NEVER store passwords as plaintext}', 1),
	('ElliotA','H3ll0Fri3nd', 1),
    ('MrRobot','fs0ci3ty', 1),
    ('Whit3Ros3','Sh1pMyPr0j3ctAlr3ady', 1),
	('TyrellW','IL0v3Elli0t', 0),
	('AngelaM','I@md3d', 0),
	('DarleneA','I@amN0tTh@tSp3ci@l', 0),
	('JWellick','I@mCr33py', 0),
	('DominiqueD','0hSh1t', 0),
	('PhillipPrice','1tsJustBus1n3ss', 0),
	('GideonG','@lls@f3', 0),
	('TerryC','Ch0k3OnMyB@lls', 0),
	('ScottK','N0tMyWif3!', 0),
	('SharonK','IC@ntBr3ath', 0),
	('KristaG','St@yAw@yFr3ak', 0),
	('ShaylaN','UW@nn@G3tH1gh?', 0),
	('Romero','1D0ntTrustY0u', 0),
	('Trenton','C@ntR3m3mb3rWh@atSh3D1d', 0),
	('Mobley','Tim3T0G0T0Th3GymM@t3', 0),
	('Cisco','D@rk@rmyC0nt@ct', 0);