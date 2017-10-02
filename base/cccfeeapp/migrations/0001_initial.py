# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annualbankdata',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('tenor4m', models.TextField(blank=True, db_column='tenor4M', null=True)),
                ('tenor9m', models.TextField(blank=True, db_column='tenor9M', null=True)),
                ('tenor12m', models.TextField(blank=True, db_column='tenor12M', null=True)),
                ('tenor6m', models.TextField(blank=True, db_column='tenor6M', null=True)),
                ('tenor18m', models.TextField(blank=True, db_column='tenor18M', null=True)),
                ('bankcode', models.TextField(blank=True, null=True)),
                ('tenor3m', models.TextField(blank=True, db_column='tenor3M', null=True)),
                ('tenor15m', models.TextField(blank=True, db_column='tenor15M', null=True)),
            ],
            options={
                'db_table': 'annualbankdata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bankinfo',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('bankname', models.TextField(blank=True, null=True)),
                ('longname', models.TextField(blank=True, null=True)),
                ('bankcode', models.TextField(blank=True, null=True)),
                ('countryname', models.TextField(blank=True, null=True)),
                ('countrycode', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bankinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Semibankdata',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('tenor4m', models.TextField(blank=True, db_column='tenor4M', null=True)),
                ('tenor9m', models.TextField(blank=True, db_column='tenor9M', null=True)),
                ('tenor12m', models.TextField(blank=True, db_column='tenor12M', null=True)),
                ('tenor6m', models.TextField(blank=True, db_column='tenor6M', null=True)),
                ('tenor18m', models.TextField(blank=True, db_column='tenor18M', null=True)),
                ('bankcode', models.TextField(blank=True, null=True)),
                ('tenor3m', models.TextField(blank=True, db_column='tenor3M', null=True)),
                ('tenor15m', models.TextField(blank=True, db_column='tenor15M', null=True)),
            ],
            options={
                'db_table': 'semibankdata',
                'managed': False,
            },
        ),
    ]
