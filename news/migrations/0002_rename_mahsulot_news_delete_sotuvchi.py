# Generated by Django 5.0.4 on 2024-04-25 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mahsulot',
            new_name='News',
        ),
        migrations.DeleteModel(
            name='sotuvchi',
        ),
    ]