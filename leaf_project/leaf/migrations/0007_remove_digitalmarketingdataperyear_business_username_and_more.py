# Generated by Django 4.2.3 on 2023-07-27 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0006_alter_spendingdataperyear_business_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='digitalmarketingdataperyear',
            name='business_username',
        ),
        migrations.RemoveField(
            model_name='ghgassessmentdataperyear',
            name='business_username',
        ),
        migrations.RemoveField(
            model_name='spendingdataperyear',
            name='business_username',
        ),
        migrations.RemoveField(
            model_name='workerpayperyear',
            name='business_username',
        ),
        migrations.AlterField(
            model_name='digitalmarketingdataperyear',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='digitalmarketingbusinesses', serialize=False, to='leaf.business'),
        ),
        migrations.AlterField(
            model_name='ghgassessmentdataperyear',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ghgassessmentbusinesses', serialize=False, to='leaf.business'),
        ),
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='spendingbusinesses', serialize=False, to='leaf.business'),
        ),
        migrations.AlterField(
            model_name='workerpayperyear',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='workerpaybusinesses', serialize=False, to='leaf.business'),
        ),
    ]