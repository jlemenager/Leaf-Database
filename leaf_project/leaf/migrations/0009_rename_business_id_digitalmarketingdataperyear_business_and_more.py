# Generated by Django 4.2.3 on 2023-07-27 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0008_digitalmarketingdataperyear_business_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='digitalmarketingdataperyear',
            old_name='business_id',
            new_name='business',
        ),
        migrations.RenameField(
            model_name='ghgassessmentdataperyear',
            old_name='business_id',
            new_name='business',
        ),
        migrations.RenameField(
            model_name='spendingdataperyear',
            old_name='business_id',
            new_name='business',
        ),
        migrations.RenameField(
            model_name='workerpayperyear',
            old_name='business_id',
            new_name='business',
        ),
    ]
