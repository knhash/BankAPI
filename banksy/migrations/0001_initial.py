# Generated by Django 2.2 on 2019-04-25 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('ifsc', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('bank_id', models.BigIntegerField()),
                ('branch', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('bank_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'bank',
            },
        ),
    ]
