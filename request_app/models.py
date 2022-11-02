from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date


class UserTypes(models.Model):
    type_name = models.CharField(max_length=4)


class Account(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserTypes, on_delete=models.CASCADE)


class DocTypeNames(models.Model):
    type_name = models.CharField(max_length=120)

    def __str__(self):
        return self.type_name


class Requests(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='id пользователя')
    doc_type = models.ForeignKey(DocTypeNames, on_delete=models.CASCADE, verbose_name='Вид бланков')
    count = models.IntegerField(blank=True, null=True, editable=True, verbose_name='Количество')
    numbers = models.CharField(max_length=30, blank=True, null=True, editable=True, verbose_name='Диапазон номеров')
    status = models.IntegerField(default=1, verbose_name='Статус заявки')
    date = models.DateField(null=True, blank=True, verbose_name='Дата подачи заявки')
    execution_date = models.DateField(null=True, blank=True, verbose_name='Дата исполнения заявки')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.account.save()
