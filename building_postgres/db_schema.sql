CREATE TABLE blogs (
  url VARCHAR(255) PRIMARY KEY NOT NULL,
  cleaning_class VARCHAR(45) NULL
);

CREATE TABLE posts (
  url VARCHAR(255) PRIMARY KEY NOT NULL,
  uuid UUID NULL,
  download_date TIMESTAMP NULL,
  blog_url VARCHAR(255) NULL references blogs(url),
  title VARCHAR(255) NULL,
  author VARCHAR(45) NULL,
  pub_date TIMESTAMP NULL,
  body TEXT NULL
);

ALTER TABLE blogs ADD COLUMN recent_post VARCHAR(255) REFERENCES posts(url);
