# Generated by Django 4.2.3 on 2023-07-27 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0007_remove_digitalmarketingdataperyear_business_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='digitalmarketingdataperyear',
            name='business_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='digitalmarketingbusinesses', to='leaf.business'),
        ),
        migrations.AddField(
            model_name='ghgassessmentdataperyear',
            name='business_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ghgassessmentbusinesses', to='leaf.business'),
        ),
        migrations.AddField(
            model_name='spendingdataperyear',
            name='business_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='spendingbusinesses', to='leaf.business'),
        ),
        migrations.AddField(
            model_name='workerpayperyear',
            name='business_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='workerpaybusinesses', to='leaf.business'),
        ),
        migrations.AlterField(
            model_name='digitalmarketingdataperyear',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ghgassessmentdataperyear',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='workerpayperyear',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
