# Generated by Django 3.2.4 on 2021-06-20 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0029_auto_20210620_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='client.user'),
        ),
    ]
