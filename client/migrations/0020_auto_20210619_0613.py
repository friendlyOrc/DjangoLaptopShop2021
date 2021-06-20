# Generated by Django 3.2.4 on 2021-06-18 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0019_auto_20210619_0541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='attrs',
        ),
        migrations.AddField(
            model_name='attribute',
            name='rate',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='client.rating'),
            preserve_default=False,
        ),
    ]
