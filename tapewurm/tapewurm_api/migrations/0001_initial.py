# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submitted', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=200)),
                ('url_identifier', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('musicbrainz_id', models.CharField(max_length=36)),
                ('order', models.PositiveIntegerField()),
                ('note', models.TextField()),
                ('mix', models.ForeignKey(to='tapewurm_api.Mix')),
            ],
        ),
    ]
