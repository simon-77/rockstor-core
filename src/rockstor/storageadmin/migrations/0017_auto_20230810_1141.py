# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-08-10 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import storageadmin.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('storageadmin', '0016_auto_20221020_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliance',
            name='hostname',
            field=models.CharField(default='Rockstor', max_length=128),
        ),
        migrations.AlterField(
            model_name='configbackup',
            name='config_backup',
            field=models.FileField(null=True, upload_to='config-backups'),
        ),
        migrations.AlterField(
            model_name='nfsexportgroup',
            name='editable',
            field=models.CharField(choices=[('ro', 'ro'), ('rw', 'rw')], default='rw', max_length=2, validators=[storageadmin.models.validators.validate_nfs_modify_str]),
        ),
        migrations.AlterField(
            model_name='nfsexportgroup',
            name='mount_security',
            field=models.CharField(choices=[('secure', 'secure'), ('insecure', 'insecure')], default='insecure', max_length=8),
        ),
        migrations.AlterField(
            model_name='nfsexportgroup',
            name='syncable',
            field=models.CharField(choices=[('async', 'async'), ('sync', 'sync')], default='async', max_length=5, validators=[storageadmin.models.validators.validate_nfs_sync_choice]),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='description',
            field=models.CharField(default='', max_length=4096),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='display_name',
            field=models.CharField(default='', max_length=4096, unique=True),
        ),
        migrations.AlterField(
            model_name='poolbalance',
            name='status',
            field=models.CharField(default='started', max_length=10),
        ),
        migrations.AlterField(
            model_name='poolscrub',
            name='rate',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='poolscrub',
            name='status',
            field=models.CharField(default='started', max_length=10),
        ),
        migrations.AlterField(
            model_name='posixacls',
            name='owner',
            field=models.CharField(choices=[('user', 'user'), ('group', 'group'), ('other', 'other')], max_length=5),
        ),
        migrations.AlterField(
            model_name='posixacls',
            name='perms',
            field=models.CharField(choices=[('r', 'r'), ('w', 'w'), ('x', 'x'), ('rw', 'rw'), ('rx', 'rx'), ('wx', 'wx'), ('rwx', 'rwx')], max_length=3),
        ),
        migrations.AlterField(
            model_name='sambashare',
            name='browsable',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=3),
        ),
        migrations.AlterField(
            model_name='sambashare',
            name='comment',
            field=models.CharField(default='foo bar', max_length=100),
        ),
        migrations.AlterField(
            model_name='sambashare',
            name='guest_ok',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=3),
        ),
        migrations.AlterField(
            model_name='sambashare',
            name='read_only',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=3),
        ),
        migrations.AlterField(
            model_name='sftp',
            name='editable',
            field=models.CharField(choices=[('ro', 'ro'), ('rw', 'rw')], default='ro', max_length=2),
        ),
        migrations.AlterField(
            model_name='share',
            name='group',
            field=models.CharField(default='root', max_length=4096),
        ),
        migrations.AlterField(
            model_name='share',
            name='owner',
            field=models.CharField(default='root', max_length=4096),
        ),
        migrations.AlterField(
            model_name='share',
            name='perms',
            field=models.CharField(default='755', max_length=9),
        ),
        migrations.AlterField(
            model_name='share',
            name='pqgroup',
            field=models.CharField(default='-1/-1', max_length=32),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='assessment',
            field=models.CharField(max_length=64, verbose_name='Overall Health Self-Assessment Test'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='ata_version',
            field=models.CharField(max_length=64, verbose_name='ATA Version'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='capacity',
            field=models.CharField(max_length=64, verbose_name='Capacity'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='device_model',
            field=models.CharField(max_length=64, verbose_name='Device Model'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='enabled',
            field=models.CharField(max_length=64, verbose_name='SMART Enabled'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='firmware_version',
            field=models.CharField(max_length=64, verbose_name='Firmware Version'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='in_smartdb',
            field=models.CharField(max_length=64, verbose_name='In Smartctl Database'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='model_family',
            field=models.CharField(max_length=64, verbose_name='Model Family'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='rotation_rate',
            field=models.CharField(max_length=64, verbose_name='Rotation Rate'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='sata_version',
            field=models.CharField(max_length=64, verbose_name='SATA Version'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='scanned_on',
            field=models.CharField(max_length=64, verbose_name='Scanned on'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='sector_size',
            field=models.CharField(max_length=64, verbose_name='Sector Size'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='serial_number',
            field=models.CharField(max_length=64, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='supported',
            field=models.CharField(max_length=64, verbose_name='SMART Supported'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='version',
            field=models.CharField(max_length=64, verbose_name='Smartctl Version'),
        ),
        migrations.AlterField(
            model_name='smartidentity',
            name='world_wide_name',
            field=models.CharField(max_length=64, verbose_name='World Wide Name'),
        ),
        migrations.AlterField(
            model_name='snapshot',
            name='real_name',
            field=models.CharField(default='unknownsnap', max_length=4096),
        ),
        migrations.AlterField(
            model_name='snapshot',
            name='snap_type',
            field=models.CharField(default='admin', max_length=64),
        ),
        migrations.AlterField(
            model_name='supportcase',
            name='case_type',
            field=models.CharField(choices=[('auto', 'auto'), ('manual', 'manual')], max_length=6),
        ),
        migrations.AlterField(
            model_name='supportcase',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('submitted', 'submitted'), ('resolved', 'resolved')], max_length=9),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=4096, unique=True),
        ),
    ]
