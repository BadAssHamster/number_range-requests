# Generated by Django 4.1.2 on 2022-10-31 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request_app', '0006_statusnames_alter_requests_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request_app.statusnames', verbose_name='Статус заявки'),
        ),
    ]
