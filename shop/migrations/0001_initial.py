# Generated by Django 4.1.10 on 2023-08-22 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categroy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200)),
            ],
            options={
                "verbose_name": "categroy",
                "verbose_name_plural": "categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200)),
                ("image", models.ImageField(blank=True, upload_to="product/%Y/%m/%d")),
                ("description", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("available", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "categroy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="shop.categroy",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.AddIndex(
            model_name="categroy",
            index=models.Index(fields=["name"], name="shop_categr_name_de9f9e_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["id", "slug"], name="shop_produc_id_f21274_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["name"], name="shop_produc_name_a2070e_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(
                fields=["-created"], name="shop_produc_created_ef211c_idx"
            ),
        ),
    ]
