# Generated by Django 5.0.6 on 2024-09-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bors", "0004_investment_profit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="investment",
            name="initial_amount",
            field=models.IntegerField(),
        ),
    ]
