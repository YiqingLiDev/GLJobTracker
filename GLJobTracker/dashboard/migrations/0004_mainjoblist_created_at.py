# Generated by Django 5.0.6 on 2024-06-28 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_mainjoblist_deadline_remove_mainjoblist_note_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainjoblist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
