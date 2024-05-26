CREATE SCHEMA "users";

CREATE TABLE "spaces" (
  "id" uuid PRIMARY KEY,
  "name" varchar,
  "description" text,
  "created_at" timestamp
);

CREATE TABLE "users" (
  "id" uuid PRIMARY KEY,
  "username" varchar,
  "password" varchar,
  "role" varchar,
  "created_at" timestamp
);

CREATE TABLE "sessions" (
  "id" uuid PRIMARY KEY,
  "title" varchar,
  "description" text,
  "space_id" uuid,
  "status" varchar,
  "timer" time,
  "created_at" timestamp
);

CREATE TABLE "tasks" (
  "id" uuid PRIMARY KEY,
  "session_id" uuid,
  "title" varchar,
  "description" text,
  "status" varchar,
  "created_at" timestamp
);

CREATE TABLE "leaderboard" (
  "id" uuid PRIMARY KEY,
  "session_id" uuid,
  "user_id" uuid,
  "score" int,
  "created_at" timestamp
);

CREATE TABLE "user_statistics" (
  "id" uuid PRIMARY KEY,
  "user_id" uuid,
  "tasks_completed" int,
  "sessions_attended" int,
  "average_session_duration" interval,
  "created_at" timestamp
);

CREATE TABLE "space_members" (
  "space_id" uuid,
  "user_id" uuid,
  "joined_at" timestamp
);

CREATE TABLE "users"."role" (
  "role_id" uuid,
  "role_name" varchar,
  "created_at" timestamp
);

COMMENT ON COLUMN "spaces"."description" IS 'Short description';

COMMENT ON COLUMN "users"."role" IS 'User role (admin/user)';

COMMENT ON COLUMN "sessions"."description" IS 'Short description';

ALTER TABLE "sessions" ADD FOREIGN KEY ("space_id") REFERENCES "spaces" ("id");

ALTER TABLE "tasks" ADD FOREIGN KEY ("session_id") REFERENCES "sessions" ("id");

ALTER TABLE "leaderboard" ADD FOREIGN KEY ("session_id") REFERENCES "sessions" ("id");

ALTER TABLE "leaderboard" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "space_members" ADD FOREIGN KEY ("space_id") REFERENCES "spaces" ("id");

ALTER TABLE "space_members" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "user_statistics" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "users"."role" ADD FOREIGN KEY ("role_id") REFERENCES "users" ("role");
