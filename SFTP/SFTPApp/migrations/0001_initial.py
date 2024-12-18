# Generated by Django 5.1.1 on 2024-11-13 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EasyDumps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminal_id', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.CharField(max_length=120)),
                ('amount', models.FloatField()),
                ('transaction_fee', models.FloatField()),
                ('easy_ref', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('payment_type', models.CharField(blank=True, max_length=100, null=True)),
                ('paid_amount', models.FloatField()),
                ('bank_cost', models.FloatField()),
                ('sof_info', models.CharField(max_length=300)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
