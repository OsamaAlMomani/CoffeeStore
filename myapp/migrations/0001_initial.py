# Generated by Django 4.1.5 on 2023-02-22 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cuisine', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
