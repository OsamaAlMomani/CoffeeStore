# Generated by Django 4.1.5 on 2023-02-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sign_in',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='sign_up',
            fields=[
                ('first_Name', models.CharField(max_length=200)),
                ('last_Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=1000, primary_key=True, serialize=False)),
                ('dob', models.DateField()),
            ],
        ),
    ]
