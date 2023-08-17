DROP SCHEMA fileretrieve CASCADE;
CREATE SCHEMA fileRetrieve;

CREATE TABLE Files (
    filename VARCHAR(255) PRIMARY KEY,
    filesize INTEGER
);