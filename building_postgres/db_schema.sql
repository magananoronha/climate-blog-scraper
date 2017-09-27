CREATE TABLE blogs (
  url VARCHAR(255) PRIMARY KEY NOT NULL,
  cleaning_class VARCHAR(255) NULL
);

CREATE TABLE posts (
  url VARCHAR(255) PRIMARY KEY NOT NULL,
  uuid UUID NULL,
  download_date TIMESTAMP NULL,
  blog_url VARCHAR(255) NULL references blogs(url),
  title VARCHAR(255) NULL,
  author VARCHAR(255) NULL,
  pub_date TIMESTAMP NULL,
  body TEXT NULL,
  prev_post VARCHAR(255) NULL,
  next_post VARCHAR(255) NULL
);

ALTER TABLE blogs ADD COLUMN recent_post VARCHAR(255) REFERENCES posts(url);
