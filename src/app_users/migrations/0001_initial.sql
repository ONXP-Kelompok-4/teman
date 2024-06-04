-- Create the Profile table
CREATE TABLE "app_users_profile" (
    "id" bigint NOT NULL PRIMARY KEY,
    "image" varchar(100) NULL,
    "displayName" varchar(200) NULL,
    "info" text NULL,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);

-- Add indexes
CREATE INDEX "app_profile_user_id" ON "app_profile" ("user_id");