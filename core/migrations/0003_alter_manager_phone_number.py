# Generated by Django 4.1 on 2024-03-18 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_company_created_at_company_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='phone_number',
            field=models.CharField(max_length=8),
        ),
    ]
