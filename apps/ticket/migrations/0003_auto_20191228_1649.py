# Generated by Django 3.0.1 on 2019-12-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20191228_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='numbers_selected',
        ),
        migrations.AddField(
            model_name='ticket',
            name='number_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='number_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='number_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='number_4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='number_5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='number_6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='number_7',
            field=models.IntegerField(default=0),
        ),
    ]