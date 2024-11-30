# Generated by Django 5.1.3 on 2024-11-29 17:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0005_remove_servicerequest_customer_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerequest',
            old_name='date_submitted',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='date_resolved',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='file_attachment',
            field=models.FileField(blank=True, null=True, upload_to='service_requests/'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='service_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('resolved', 'Resolved')], max_length=50),
        ),
    ]