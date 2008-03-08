-- Migrate to using django-voting instead of the built-in vote package.

BEGIN;

CREATE TABLE "new_votes" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED,
    "object_id" integer CHECK ("object_id" >= 0) NOT NULL,
    "vote" smallint NOT NULL,
    UNIQUE ("user_id", "content_type_id", "object_id")
);

INSERT INTO new_votes 
    SELECT 
        id, 
        user_id, 
        content_type_id, 
        object_pk::INTEGER AS object_id, 
        vote 
    FROM votes;
    
DROP TABLE votes;

ALTER TABLE new_votes RENAME TO votes;

COMMIT;