# Generated by Django 5.0.1 on 2024-01-21 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameIndex(
            model_name='comment',
            new_name='blogapp_com_created_22385d_idx',
            old_name='blogapp_com_created_91397e_idx',
        ),
    ]