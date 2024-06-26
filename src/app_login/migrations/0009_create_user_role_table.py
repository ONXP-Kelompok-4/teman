# Generated by Django 5.0.6 on 2024-05-26 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0008_create_space_member_table'),
    ]

    operations = [migrations.RunSQL(
        sql=[
            ("""CREATE TABLE "users"."role" (
             "role_id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
             "role_name" varchar NOT NULL,
             "created_at" timestamp NOT NULL DEFAULT NOW()
             );"""),

             ("""ALTER TABLE "users"
              ADD CONSTRAINT fk_role_id
              FOREIGN KEY ("role_id")
              REFERENCES "users"."role" ("role_id");
              """),
             ],
        reverse_sql=[
            ("""ALTER TABLE "users"
             DROP CONSTRAINT IF EXISTS fk_role_id;
             DROP TABLE IF EXISTS users.role;"""),
            ]
            )
    ]
