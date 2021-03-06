# Generated by Django 3.0 on 2021-05-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationinfo',
            name='days_count',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationinfo',
            name='donated_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationinfo',
            name='required_tablets',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationinfo',
            name='total_tablets',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
