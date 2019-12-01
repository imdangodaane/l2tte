from rest_framework import serializers
from api.account.models import Login


class RegisterAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['userid', 'user_pass', 'sex', 'email', 'birthdate']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['userid', 'user_pass']


class AccountInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = [
            'account_id',
            'userid',
            'sex',
            'email',
            'group_id',
            'state',
            'logincount',
            'lastlogin',
            'last_ip',
            'birthdate',
            'character_slots',
            'vip_time',
            'old_group'
        ]
