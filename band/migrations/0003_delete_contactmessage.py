# Generated by Django 5.0.1 on 2024-04-02 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0002_contactmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactMessage',
        ),
    ]
