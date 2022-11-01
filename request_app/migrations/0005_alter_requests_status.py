# Generated by Django 4.1.2 on 2022-10-31 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_app', '0004_alter_requests_date_alter_requests_execution_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='status',
            field=models.IntegerField(choices=[(1, 'Черновик'), (2, 'Отправлена'), (3, 'Выполнена')], default=1, verbose_name='Статус заявки'),
        ),
    ]