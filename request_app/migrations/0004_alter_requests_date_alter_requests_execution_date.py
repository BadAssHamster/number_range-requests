# Generated by Django 4.1.2 on 2022-10-29 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_app', '0003_alter_requests_count_alter_requests_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата подачи заявки'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='execution_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата исполнения заявки'),
        ),
    ]
