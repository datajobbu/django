# Generated by Django 3.1.3 on 2021-01-28 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('sum_amt_1d', models.CharField(max_length=30)),
                ('sum_cnt_1d', models.CharField(max_length=5)),
                ('cnt_opp_1d', models.CharField(max_length=5)),
                ('aml_code', models.CharField(max_length=10)),
                ('code_name', models.CharField(max_length=50)),
                ('report_date', models.CharField(max_length=20)),
            ],
        ),
    ]