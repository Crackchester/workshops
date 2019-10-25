CREATE TABLE ctf_workshop_dev.Users (
  `username` varchar(245) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO ctf_workshop_dev.Users (username, password)
VALUES
	('TodaysLesson','NEVER store passwords as plaintext'),
	('ElliotA','H3ll0Fri3nd'),
    ('MrRobot','fs0ci3ty'),
    ('Whit3Ros3','Sh1pMyPr0j3ctAlr3ady'),
	('TyrellW','IL0v3Elli0t'),
	('AngelaM','I@md3d'),
	('DarleneA','I@amN0tTh@tSp3ci@l'),
	('JWellick','I@mCr33py'),
	('DominiqueD','0hSh1t'),
	('PhillipPrice','1tsJustBus1n3ss'),
	('GideonG','@lls@f3'),
	('TerryC','Ch0k3OnMyB@lls'),
	('ScottK','N0tMyWif3!'),
	('SharonK','IC@ntBr3ath'),
	('KristaG','St@yAw@yFr3ak'),
	('ShaylaN','UW@nn@G3tH1gh?'),
	('Romero','1D0ntTrustY0u'),
	('Trenton','C@ntR3m3mb3rWh@atSh3D1d'),
	('Mobley','Tim3T0G0T0Th3GymM@t3'),
	('Cisco','D@rk@rmyC0nt@ct')