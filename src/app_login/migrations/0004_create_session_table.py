# Generated by Django 5.0.6 on 2024-05-26 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0003_create_user_table'),
    ]

    operations = [migrations.RunSQL(
        sql=[
            ("""CREATE TABLE IF NOT EXISTS "sessions" (
             "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
             "title" varchar NOT NULL,
             "description" text,
             "space_id" uuid NOT NULL,
             "status" varchar NOT NULL,
             "timer" time,
             "created_at" timestamp NOT NULL DEFAULT NOW(),
             FOREIGN KEY ("space_id") REFERENCES "spaces" ("id")
             );"""),
             ("""CREATE INDEX idx_sessions_space_id ON "sessions" ("space_id");"""),
             ],
        reverse_sql=[
            ("""DROP INDEX IF EXISTS idx_sessions_space_id;"""),
            ("""DROP TABLE IF EXISTS "sessions";"""),
            ]
            )
    ]
