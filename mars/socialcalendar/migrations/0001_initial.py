# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caldata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site', models.IntegerField(max_length=11)),
                ('month', models.CharField(max_length=20, null=True)),
                ('vtlid', models.IntegerField(max_length=11, null=True)),
                ('vtlname', models.CharField(max_length=1000, null=True)),
                ('lv1id', models.IntegerField(max_length=11, null=True)),
                ('lv1name', models.CharField(max_length=1000, null=True)),
                ('lv2id', models.IntegerField(max_length=11, null=True)),
                ('lv2name', models.CharField(max_length=1000, null=True)),
                ('lv3id', models.IntegerField(max_length=11, null=True)),
                ('lv3name', models.CharField(max_length=1000, null=True)),
                ('lv4id', models.IntegerField(max_length=11, null=True)),
                ('lv4name', models.CharField(max_length=1000, null=True)),
                ('lvleafid', models.IntegerField(max_length=11, null=True)),
                ('lvleafname', models.CharField(max_length=1000, null=True)),
                ('power', models.DecimalField(null=True, max_digits=16, decimal_places=2)),
                ('bi', models.DecimalField(null=True, max_digits=32, decimal_places=16)),
                ('gmb', models.DecimalField(null=True, max_digits=32, decimal_places=16)),
                ('bisnr', models.DecimalField(null=True, max_digits=16, decimal_places=2)),
                ('gmbsnr', models.DecimalField(null=True, max_digits=16, decimal_places=2)),
            ],
            options={
                'verbose_name': 'SocialCalendar',
            },
        ),
    ]
