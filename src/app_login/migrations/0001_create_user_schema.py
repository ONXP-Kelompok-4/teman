# Generated by Django 5.0.6 on 2024-05-26 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [migrations.RunSQL(
        sql=[
            ("CREATE SCHEMA 'users'"),
             ],
        reverse_sql=[
            ("DROP SCHEMA IF EXISTS 'users' CASCADE"),
            ]
            )
    ]
