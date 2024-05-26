# Generated by Django 5.0.6 on 2024-05-26 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0006_create_leaderboard_table'),
    ]

    operations = [migrations.RunSQL(
        sql=[
            ("""CREATE TABLE IF NOT EXISTS "user_statistics" (
             "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
             "user_id" uuid NOT NULL,
             "tasks_completed" int NOT NULL,
             "sessions_attended" int NOT NULL,
             "average_session_duration" interval NOT NULL,
             "created_at" timestamp NOT NULL DEFAULT NOW(),
             FOREIGN KEY ("user_id") REFERENCES "users" ("id")
             );"""),
             ("""CREATE INDEX idx_user_statistics_user_id ON "user_statistics" ("user_id");"""),
             ],
        reverse_sql=[
            ("""DROP INDEX IF EXISTS idx_user_statistics_user_id;"""),
            ("""DROP TABLE IF EXISTS "user_statistics";"""),
            ]
            )
    ]
