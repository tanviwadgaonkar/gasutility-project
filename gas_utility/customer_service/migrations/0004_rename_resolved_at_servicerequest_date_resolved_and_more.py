# Generated by Django 5.1.3 on 2024-11-28 19:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0003_rename_description_servicerequest_details_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerequest',
            old_name='resolved_at',
            new_name='date_resolved',
        ),
        migrations.RenameField(
            model_name='servicerequest',
            old_name='created_at',
            new_name='date_submitted',
        ),
        migrations.RenameField(
            model_name='servicerequest',
            old_name='details',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='attached_file',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='email',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='file_attachment',
            field=models.FileField(blank=True, null=True, upload_to='service_requests/'),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='resolved_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='service_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='Pending', max_length=20),
        ),
    ]
