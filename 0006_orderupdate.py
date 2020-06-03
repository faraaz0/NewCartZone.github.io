# Generated by Django 3.0.6 on 2020-06-02 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200601_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderupdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=500)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]