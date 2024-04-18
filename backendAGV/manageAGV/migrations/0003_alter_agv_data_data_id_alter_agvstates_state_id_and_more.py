# Generated by Django 4.1 on 2024-04-18 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageAGV', '0002_db_stationdata_orderdata_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agv_data',
            name='data_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='agvstates',
            name='state_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dataschedule',
            name='schedule_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderdata',
            name='request_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]