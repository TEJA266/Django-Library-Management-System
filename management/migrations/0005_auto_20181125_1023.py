# Generated by Django 2.1.3 on 2018-11-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20181125_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='issue_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='borrower',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
