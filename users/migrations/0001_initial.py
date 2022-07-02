# Generated by Django 4.0.3 on 2022-06-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('username', models.TextField()),
                ('birth', models.TextField()),
                ('gender', models.TextField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
