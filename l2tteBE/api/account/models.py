from django.db import models
from django.utils import timezone
from datetime import timedelta


class Login(models.Model):
    account_id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=23)
    user_pass = models.CharField(max_length=32)
    sex = models.CharField(max_length=1)
    email = models.CharField(max_length=39)
    group_id = models.IntegerField(default=0)
    state = models.PositiveIntegerField(default=0)
    unban_time = models.PositiveIntegerField(default=0)
    expiration_time = models.PositiveIntegerField(default=0)
    logincount = models.PositiveIntegerField(default=0)
    lastlogin = models.DateTimeField(blank=True, null=True)
    last_ip = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    character_slots = models.PositiveIntegerField(default=0)
    pincode = models.CharField(max_length=4)
    pincode_change = models.PositiveIntegerField(default=0)
    vip_time = models.PositiveIntegerField(default=0)
    old_group = models.IntegerField(default=0)
    is_authenticated = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'login'

    def __str__(self):
        return '_'.join([str(self.account_id), self.userid])


class Token(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    expired_at = models.DateTimeField(
        default=timezone.now() + timedelta(minutes=15), blank=True, null=True)

    def __str__(self):
        return 'of userid: ' + str(self.user.account_id)
