# Generated by Django 4.1.5 on 2023-03-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_coffee_dessert_meal_rename_orders_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee',
            name='Coffee_Id',
        ),
        migrations.RemoveField(
            model_name='dessert',
            name='Dessert_Id',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='Meal_Id',
        ),
        migrations.AlterField(
            model_name='coffee',
            name='Coffee_Describtion',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='Coffee_Name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dessert',
            name='Dessert_Describtion',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='dessert',
            name='Dessert_Name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='meal',
            name='Meal_Describtion',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='meal',
            name='Meal_Name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
