# Generated by Django 3.2.4 on 2021-06-17 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_attribute_category_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=224, null=False)),
                ('price', models.FloatField(blank=True, default='', max_length=224, null=False)),
                ('des', models.CharField(blank=True, default='', max_length=224, null=False)),
                ('year', models.IntegerField(default=0)),
                ('screen', models.FloatField(blank=True, default='', max_length=224, null=False)),
                ('image', models.CharField(blank=True, default='', max_length=224, null=False)),
                ('battery', models.IntegerField(default=0)),
                ('memory', models.FloatField(blank=True, default=0, max_length=224, null=False)),
                ('ram', models.IntegerField(default=0)),
                ('os', models.CharField(blank=True, default='', max_length=224, null=False)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client.category')),
                ('rate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client.rating')),
            ],
        ),
    ]
