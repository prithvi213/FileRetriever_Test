DROP SCHEMA fileretrieve CASCADE;
CREATE SCHEMA fileRetrieve;

CREATE TABLE Files (
    filename TEXT PRIMARY KEY,
    filesize INTEGER,
    directory TEXT
);