# Generated by Django 2.2.6 on 2019-10-23 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golf', '0003_club'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Club',
            new_name='GolfClub',
        ),
    ]