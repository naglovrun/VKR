# -*- coding: utf8 -*-
from django.db import models


class Client(models.Model):
    familiya = models.CharField(max_length=20, verbose_name='Фамилия клиента')
    imya = models.CharField(max_length=20, verbose_name='Имя клиента')
    otchestvo = models.CharField(max_length=20, verbose_name='Отчество клиента', blank=True, null=True)
    vozrast = models.IntegerField(max_length=20, verbose_name='Возраст')
    skidki = models.CharField(max_length=20, verbose_name='Скидки', blank=True, null=True)

    # def __unicode__(self):
    #     return self.imya  + ' ' + self.familiya

    def __str__(self):
        return self.imya + ' ' + self.familiya

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Bilet(models.Model):
    kodbileta = models.IntegerField(verbose_name='КодБилета') #TODO uberi mena
    nomerzala = models.ForeignKey('Zaly', related_name='bilets')
    сlient = models.ForeignKey(Client, related_name='bilets')


class Zaly(models.Model):
    nomerzala = models.IntegerField(max_length=10, verbose_name='Номер зала')
    nomermesta = models.IntegerField(max_length=10,verbose_name='Ноаер места')
    nomerryada = models.IntegerField(max_length=10, verbose_name='Номер ряда')
