# Generated by Django 5.0.6 on 2024-06-27 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_mainjoblist_deadline_alter_mainjoblist_note_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainjoblist',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='mainjoblist',
            name='note',
        ),
        migrations.RemoveField(
            model_name='mainjoblist',
            name='url_link',
        ),
    ]
