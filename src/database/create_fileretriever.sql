DROP SCHEMA FileRetriever CASCADE;
CREATE SCHEMA FileRetriever;

CREATE TABLE Files (
    filename VARCHAR(255) PRIMARY KEY,
    filesize INTEGER
);