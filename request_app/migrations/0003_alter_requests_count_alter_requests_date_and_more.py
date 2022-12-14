# Generated by Django 4.1.2 on 2022-10-29 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request_app', '0002_alter_requests_execution_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата подачи заявки'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='doc_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request_app.doctypenames', verbose_name='Вид бланков'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='execution_date',
            field=models.DateField(null=True, verbose_name='Дата исполнения заявки'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='numbers',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Диапазон номеров'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='status',
            field=models.IntegerField(default=1, verbose_name='Статус заявки'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request_app.account', verbose_name='id пользователя'),
        ),
    ]
