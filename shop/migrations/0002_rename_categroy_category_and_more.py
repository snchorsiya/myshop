# Generated by Django 4.1.10 on 2023-08-22 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Categroy",
            new_name="Category",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="categroy",
            new_name="category",
        ),
        migrations.RenameIndex(
            model_name="category",
            new_name="shop_catego_name_289c7e_idx",
            old_name="shop_categr_name_de9f9e_idx",
        ),
    ]
