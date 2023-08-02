# Generated by Django 4.2.3 on 2023-07-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0011_alter_spendingdataperyear_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='digitalmarketingdataperyear',
            name='business_name',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='ghgassessmentdataperyear',
            name='business_name',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='spendingdataperyear',
            name='business_name',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='workerpayperyear',
            name='business_name',
            field=models.CharField(default='none', max_length=100),
        ),
    ]