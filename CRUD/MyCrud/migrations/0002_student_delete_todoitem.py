# Generated by Django 5.2.3 on 2025-07-02 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCrud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('year_graduated', models.IntegerField(max_length=4)),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
                ('job_title', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('start_employment_date', models.DateField(blank=True, null=True)),
                ('end_employment_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TodoItem',
        ),
    ]
