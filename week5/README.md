### 第二題 建立資料庫和資料表
```CREATE DATABASE website;
USE website;
CREATE TABLE member(
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL,
	username VARCHAR(255) NOT NULL,
	password VARCHAR(255) NOT NULL,
	follower_count INT unsigned NOT NULL DEFAULT 0,
	time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
	);
```

 ![image](https://github.com/lili05020502/first-stage/assets/127928553/9effd19f-0acb-44a7-a415-fbf2d1ba83c8)

### 第三題 SQL CRUD
```
USE website;
INSERT INTO member(name,username,password) VALUES('test','test','test');

INSERT INTO member(name,username,password,follower_count,time) VALUES
('atest','atest','atest',10,'2023-1-1 00:00:00'),
('btest','btest','btest',9,'2023-2-2 00:00:00'),
('ctest','ctest','ctest',8,'2023-3-3 00:00:00'),
('dtest','dtest','dtest',7,'2023-1-4 00:00:00');

SELECT * FROM member;
SELECT * FROM member ORDER BY time DESC;
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
SELECT * FROM member WHERE username='test';
SELECT * FROM member WHERE username='test'and password='test';
UPDATE member SET name='test2' WHERE username='test';


#SELECT *FROM website.member WHERE name='test2';
```
#### 3-1 
![image](https://github.com/lili05020502/first-stage/assets/127928553/baa6f809-87d4-4cf5-884f-16dab5316cca)
#### 3-2
![image](https://github.com/lili05020502/first-stage/assets/127928553/ba650076-735b-4872-a6b8-a9d5443bade7)
#### 3-3
![image](https://github.com/lili05020502/first-stage/assets/127928553/7a6a43fb-255e-4ea5-8c85-ce0238008f0a)
#### 3-4
![image](https://github.com/lili05020502/first-stage/assets/127928553/acfdd426-49b4-4619-a752-c78f1d4c1926)
#### 3-5
![image](https://github.com/lili05020502/first-stage/assets/127928553/b56b7597-ae17-4f1e-a463-8ecb0449c8e1)
#### 3-6
![image](https://github.com/lili05020502/first-stage/assets/127928553/e608ae5e-5232-4d7b-9b13-b3e9b01f15c4)
#### 3-7
![image](https://github.com/lili05020502/first-stage/assets/127928553/67d2dfe1-945a-4297-aee8-74165a198158)

### 第四題 SQL Aggregate Functions
```
---4-1
SELECT count(*) FROM member;
SELECT COUNT(*) AS total_members FROM member;

---4-2
SELECT SUM(follower_count) AS total_followers FROM member;
---4-3
SELECT AVG(follower_count) AS average_followers FROM member;
```
#### 4-1
![image](https://github.com/lili05020502/first-stage/assets/127928553/73603ce3-8b47-42be-b899-da49aeeaace6)
#### 4-2
![image](https://github.com/lili05020502/first-stage/assets/127928553/97ea1208-3252-4ec9-8b3d-d81f224e516a)
#### 4-3
![image](https://github.com/lili05020502/first-stage/assets/127928553/a08109cf-5743-4f1c-ac1e-a7d06a2446cf)

### 第五題 SQL JOIN
```
-----建立新資料表message,外鍵對應 member 資料表中的 id
CREATE TABLE message(
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
	member_id BIGINT NOT NULL,
	content VARCHAR(255) NOT NULL,
	like_count INT unsigned NOT NULL DEFAULT 0,
	time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-----外鍵對應 member 資料表中的 id
ALTER TABLE message ADD FOREIGN KEY(member_id) REFERENCES member(id);

---建立留言
INSERT INTO message (member_id,content,like_count)VALUES
(1,'I am test',11),
(3,'I am b',33),
(2,'I am a',22),
(4,'I am c',44),
(5,'I am d',55);


---
INSERT INTO message (member_id,content,like_count)VALUES
(1,'I am test haha',111),
(3,'I am b haha',333),
(2,'I am a haha',222),
(4,'I am c haha',444),
(5,'I am d haha',555);

---5-1
SELECT member.name,message.content FROM member INNER JOIN message ON member.id=message.member_id;

---5-2
SELECT member.name,message.content FROM member INNER JOIN message ON member.id=message.member_id and member.username='test';

---5-3
SELECT member.username,AVG(message.like_count) AS average_like_count FROM member  JOIN message ON member.id=message.member_id WHERE member.username='test';

```
#### 建立新資料表message
![image](https://github.com/lili05020502/first-stage/assets/127928553/2f372622-cde7-401b-a32a-8b599c66bc79)

####外鍵對應 member 資料表中的 id
![image](https://github.com/lili05020502/first-stage/assets/127928553/a0da42d0-0298-4d2a-a4c4-8cc598f17725)


#### 建立留言
![image](https://github.com/lili05020502/first-stage/assets/127928553/5d0a950d-144b-4c69-b853-35d98c74d695)
![image](https://github.com/lili05020502/first-stage/assets/127928553/fcbbe0c9-e58b-4b0a-935a-9b3e70f1e8b6)

#### 5-1
![image](https://github.com/lili05020502/first-stage/assets/127928553/d846eb8f-453d-40a9-bf41-47585211c6a1)

#### 5-2
![image](https://github.com/lili05020502/first-stage/assets/127928553/167f96c8-c91b-439c-befa-5a64bc7f6d0d)

#### 5-3
![image](https://github.com/lili05020502/first-stage/assets/127928553/90ac17a9-64d0-4c07-9c21-aa284838d59b)






