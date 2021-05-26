# Generated by Django 3.2.3 on 2021-05-24 17:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_rename_cart_cartitems_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='category',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.cart'),
            preserve_default=False,
        ),
    ]