# Generated by Django 4.0.5 on 2022-12-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0019_remove_usermodel_user_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintmodel',
            name='Approx_date_block_chain',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='complaintmodel',
            name='Complaint_type_block_chain',
            field=models.CharField(help_text='complaint_type', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='complaintmodel',
            name='occured_place_block_chain',
            field=models.CharField(help_text='occured_place', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='complaintmodel',
            name='suspect_block_chain',
            field=models.CharField(help_text='suspect_block_chain', max_length=100, null=True),
        ),
    ]