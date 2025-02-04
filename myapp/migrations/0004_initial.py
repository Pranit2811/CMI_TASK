# Generated by Django 4.2.13 on 2024-07-15 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0003_delete_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=255)),
                ('year_founded', models.IntegerField()),
                ('industry', models.CharField(max_length=100)),
                ('size_range', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('linkedin_url', models.CharField(max_length=255)),
                ('current_employee_estimate', models.IntegerField()),
                ('total_employee_estimate', models.IntegerField()),
            ],
        ),
    ]
