CREATE TABLE Posts
    (PostID int NOT NULL IDENTITY(1,1),
    SitePostID varchar(25) NOT NULL,
    PostName varchar(75) NOT NULL,
    PostDescription varchar(max) NULL,
    Cost varchar(25) NULL,
    PostLocation varchar(50) NULL,
    CustomerMobile varchar(25) NULL,
    CustomerName varchar(25) NULL,
    SiteName varchar(35) NOT NULL,
    PostURL varchar(55) NOT NULL,
    Category varchar(45) NOT NULL,
    PostCreatedDate DATETIME NOT NULL,
    PostModifiedDate DATETIME NULL,
    PostScrapedDate DATETIME NOT NULL,
    PostExpiry varchar(1) NOT NULL,
    ActiveStatus varchar(1) NOT NULL,
     PRIMARY KEY(PostID),
     UNIQUE(SitePostID)
     )
GO

DROP TABLE Posts

select * from dbo.Posts

INSERT INTO DBO.Posts (SitePostID,PostName,PostDescription,Cost,PostLocation,SiteName,PostURL,Category,PostCreatedDate,PostScrapedDate,PostExpiry,ActiveStatus)
VALUES('123124','TEST','TEST TEST TESTDESC','KD 53','SALMIYA','IIK','HTTPS://IIK/','ROOM FOR RENT',GETDATE(),GETDATE(),'F','A')