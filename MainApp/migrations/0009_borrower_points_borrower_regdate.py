# Generated by Django 5.0.2 on 2024-03-17 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_book_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='Points',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='borrower',
            name='RegDate',
            field=models.DateField(auto_now=True),
        ),
    ]
