CREATE DATABASE IF NOT EXISTS test;
CREATE TABLE IF NOT EXISTS test.word(
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(100)
);

INSERT INTO test.word(title) VALUES('先端課題031');
INSERT INTO test.word(title) VALUES('完了です');
INSERT INTO test.word(title) VALUES('お疲れ様でした');