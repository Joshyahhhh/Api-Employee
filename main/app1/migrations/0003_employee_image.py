# Generated by Django 5.0.6 on 2024-05-19 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_employee_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
