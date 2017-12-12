# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers         # 一个实现代码高亮的模块
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS]) # 得到所有编程语言的选项
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())     # 列出所有配色风格


class person(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)



class profit(models.Model):
    year = models.CharField(max_length=20, blank=True, null=True)
    quarter = models.CharField(max_length=20, blank=True, null=True)
    stk_code = models.CharField(max_length=50, blank=True, null=True)
    stk_name = models.CharField(max_length=50, blank=True, null=True)
    roe = models.CharField(max_length=50, blank=True, null=True)
    netmargin = models.CharField(max_length=50, blank=True, null=True)
    grossmargin = models.CharField(max_length=50, blank=True, null=True)
    netprofit = models.CharField(max_length=50, blank=True, null=True)
    eps = models.CharField(max_length=50, blank=True, null=True)
    imcome = models.CharField(max_length=50, blank=True, null=True)
    imcompershare_field = models.CharField(db_column='imcompershare ', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    # id = models.IntegerField(unique=True, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'profit'