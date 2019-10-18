from django.db import models
from django.urls import reverse


# Create your models here.

class Boss(models.Model):
    class Meta:
        db_table = 'boss'

    event_month   = models.DateField(verbose_name='開催月', max_length=255)
    boss_number   = models.IntegerField(verbose_name='番号')
    boss_name     = models.CharField(verbose_name='ボス名', max_length=255)
    max_hit_point = models.IntegerField(verbose_name='HP')
    target        = models.CharField(verbose_name='ダメージ目安', max_length=255)

    def __str__(self):
        ret = self.boss_name
        return ret

    def get_absolute_url(self):
        return reverse("clanbattle:index")

class ClanMembers(models.Model):
    class Meta:
        db_table = 'clan_members'

    user_id   = models.CharField(verbose_name='ユーザID', max_length=255)
    user_name = models.CharField(verbose_name='ユーザ名', max_length=255)
    is_member = models.BooleanField(verbose_name='正式メンバー', default=False)


    def __str__(self):
        ret = self.user_name
        return ret

class BossReserve(models.Model):
    class Meta:
        db_table = 'boss_reserve'

    reserved_at = models.DateTimeField(verbose_name='予約日')
    user_id     = models.CharField(verbose_name='ユーザID', max_length=255)
    boss_number = models.IntegerField(verbose_name='番号')
    is_attack   = models.BooleanField(verbose_name='凸済み',     default=False)
    is_cancel   = models.BooleanField(verbose_name='キャンセル', default=False)


    def __str__(self):
        ret = self.user_id
        return ret


class AttackLog(models.Model):
    class Meta:
        db_table = 'attack_log'

    attack_time   = models.DateTimeField(verbose_name='凸時間')
    user_id       = models.CharField(verbose_name='ユーザID', max_length=255)
    boss_number   = models.IntegerField(verbose_name='番号')
    damage        = models.IntegerField(verbose_name='ダメージ')
    score         = models.IntegerField(verbose_name='スコア')
    is_carry_over = models.IntegerField(verbose_name='持ち越し')

    def __str__(self):
        ret = self.user_id
        return ret

class CurrentBoss(models.Model):
    class Meta:
        db_table = 'current_boss'

    boss_number = models.IntegerField(verbose_name='番号')
    hit_point   = models.IntegerField(verbose_name='残りHP')

    def __str__(self):
        ret = self.boss_number
        return ret


class CarryOver(models.Model):
    class Meta:
        db_table = 'carry_over'

    carried_at  = models.DateTimeField(verbose_name='処理日')
    user_id     = models.CharField(verbose_name='ユーザID', max_length=255)
    boss_number = models.IntegerField(verbose_name='番号')
    time        = models.IntegerField(verbose_name='持ち越し時間')
    is_attack   = models.BooleanField(verbose_name='凸済み', default=False)

    def __str__(self):
        ret = self.user_id
        return ret
