# Generated by Django 3.0.2 on 2020-01-22 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Timestamp',
            new_name='timestamp',
        ),
    ]