from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Type(models.TextChoices):
    ERROR = '0', _('오류신고')
    IMPROVE = '1', _('기능개선')
    INQUIRE = '2', _('데이터 문의')
    ANSWER = '3', _('답변')


class TblistInquire(models.Model):
    name = models.CharField(max_length=20, null=False, verbose_name='사용자 명')
    email = models.EmailField(max_length=128, null=False, verbose_name='사용자 이메일')
    content = models.CharField(max_length=2000, null=False)
    parent = models.ForeignKey('self', verbose_name='부모id', null=True, blank=True, on_delete=models.CASCADE)
    is_send_email = models.BooleanField(default=False)
    send_email_date = models.DateTimeField(null=True)
    is_answer = models.BooleanField(default=False)
    reg_user = models.CharField(max_length=20, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    update_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    update_date = models.DateTimeField(null=True)

    type = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.ERROR,
    )

    class Meta:
        db_table = 'tblist_inquire'
