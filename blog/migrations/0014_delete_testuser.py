# Generated by Django 4.2 on 2024-03-09 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_testuser_delete_student_alter_post_managers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestUser',
        ),
    ]
