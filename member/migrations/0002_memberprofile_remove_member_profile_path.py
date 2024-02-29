# Generated by Django 5.0.2 on 2024-02-29 11:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('profile_path', models.ImageField(upload_to='member/%Y/%m/%d')),
                ('member_privacy_agree', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'tbl_member_profile',
            },
        ),
        migrations.RemoveField(
            model_name='member',
            name='profile_path',
        ),
    ]