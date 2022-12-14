# Generated by Django 4.1.2 on 2022-10-31 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request_app', '0005_alter_requests_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='requests',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='request_app.statusnames', verbose_name='Статус заявки'),
        ),
    ]
