DROP DATABASE IF EXISTS GIFTCHEMIST;
CREATE DATABASE GIFTCHEMIST;
USE GIFTCHEMIST;

Create table Users(
UserId Varchar(25)not null unique,
Fname Varchar(30),
Lname Varchar(30),
Primary key(UserId)
);
Create table Access(
UserId Varchar(25)not null unique,
Username Varchar(30) unique,
Password Varchar(100),
Active varchar (15),
Primary key(UserId),
Foreign key (UserId) REFERENCES Users(UserId) ON DELETE CASCADE
);

Create table Coupon(
CoupId Varchar(25)not null unique,
Creation_date date,
Expiration_date Date,
Value int,
Redemed Varchar(10),
Primary key(CoupId)
);

Create table Redemed(
UserId Varchar(25),
CoupId Varchar(25),
Date_redemed date,
Primary key(UserId,CoupId),
Foreign key (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
Foreign key (CoupId) REFERENCES Coupon(CoupId) ON DELETE CASCADE
);

insert into Users values('UID1','Admin','Admin');
insert into Access values('UID1','IamAdmin',SHA2('admin', 256),'true');

insert into Coupon values('CUID1',"2020-01-10","2020-01-20",100, "false");
insert into Coupon values('CUID2',"2020-01-10","2020-01-20",100, "false");
insert into Coupon values('CUID3',"2020-01-10","2020-01-20",100, "true");
insert into Coupon values('CUID4',"2020-01-10","2020-01-20",100, "true");


DELIMITER //
CREATE PROCEDURE Redeem(in coupId Varchar(25),UserId Varchar(25))

begin
	UPDATE Coupon SET Redemed='true' WHERE Coupon.CoupId=coupId;
	insert into Redemed values(UserId,CoupId,now());
	
	select "Coupon Redemed Successfully";
	COMMIT;

end //

DELIMITER ;