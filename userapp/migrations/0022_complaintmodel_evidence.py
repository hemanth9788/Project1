# Generated by Django 4.0.5 on 2022-12-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0021_alter_complaintmodel_approx_date_block_chain_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintmodel',
            name='Evidence',
            field=models.FileField(default=None, max_length=500, upload_to=None),
        ),
    ]