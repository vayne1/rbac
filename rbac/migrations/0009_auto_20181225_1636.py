# Generated by Django 2.1.3 on 2018-12-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0008_auto_20181225_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='URL别名'),
        ),
    ]
