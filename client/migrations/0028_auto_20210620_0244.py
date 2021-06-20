# Generated by Django 3.2.4 on 2021-06-19 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0027_order_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fullname',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, default='', max_length=224, null=True),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rating',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reply',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
    ]
