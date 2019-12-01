# DJANGO IMPORT
from django.shortcuts import render, get_object_or_404
from django.utils import timezone as dj_timezone

# EXTERNAL IMPORT
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime, timezone, timedelta
import jwt

# FROM IMPORT
from api.account.models import Login, Token
from api.account.serializers import RegisterAccountSerializer, LoginSerializer, AccountInfoSerializer
from api.services.gzip_service import res_by_gzip
from api.services.response_service import gen_res
from api.services.authentication import AccountAuthentication

with open('./assets/jwt-key') as f:
    private_key = f.read()
with open('./assets/jwt-key.pub') as f:
    public_key = f.read()


class RegisterAccountView(generics.CreateAPIView):
    error_ref = {
        0: 'unknown error',
        1: 'unable to parse birthdate',
        2: 'userid existed',
        3: 'email existed',
        4: 'invalid payload'
    }
    status_ref = {
        0: 'success',
        1: 'fail',
        2: 'existed'
    }

    def post(self, request, *args, **kwargs):
        payload = request.data.copy()
        # VALIDATE birthdate
        try:
            payload['birthdate'] = datetime.fromisoformat(payload['birthdate'].replace(
                'Z', '+00:00')).replace(tzinfo=timezone.utc).astimezone(tz=None).date()
        except KeyError:
            return Response(gen_res(self.status_ref[1], 400, detail=self.error_ref[1]), status=400)

        serializer = RegisterAccountSerializer(data=payload)
        if serializer.is_valid():
            # VALIDATE userid
            try:
                existed_instance = Login.objects.get(userid=payload['userid'])
                return Response(gen_res(self.status_ref[2], 400, detail=self.error_ref[2]), status=400)
            except Login.DoesNotExist:
                pass

            # VALIDATE email
            try:
                existed_instance = Login.objects.get(email=payload['email'])
                return Response(gen_res(self.status_ref[2], 400, detail=self.error_ref[3]), status=400)
            except Login.DoesNotExist:
                pass

            # CREATE instance
            instance = Login(**serializer.validated_data)
            instance.save()
            return res_by_gzip(gen_res(self.status_ref[0], 200))
        return Response(gen_res(self.status_ref[1], 400, detail=self.error_ref[4]), status=400)


class LoginCheckView(generics.CreateAPIView):
    error_ref = {
        0: 'unknown error',
        1: 'unable to parse birthdate',
        2: 'userid existed',
        3: 'email existed',
        4: 'invalid payload'
    }
    status_ref = {
        0: 'success',
        1: 'fail',
        2: 'existed'
    }

    def post(self, request, *args, **kwargs):
        payload = request.data.copy()
        serializer = LoginSerializer(data=payload)
        print('aaaaaaaaaaaa')
        if serializer.is_valid():
            user = get_object_or_404(Login, userid=serializer.validated_data['userid'])
            if user and user.user_pass == serializer.validated_data['user_pass']:
                created_at = dj_timezone.now()
                expired_at = dj_timezone.now() + timedelta(minutes=15)
                token = jwt.encode({
                    'id': user.account_id,
                    'exp_iso': expired_at.isoformat()
                }, private_key, algorithm='RS256')
                try:
                    _token = Token.objects.get(user=user)
                    _token.token = token.decode('utf-8')
                    _token.created_at = created_at
                    _token.expired_at = expired_at
                except Token.DoesNotExist:
                    _token = Token(user=user, token=token.decode('utf-8'))
                _token.save()
                return res_by_gzip(gen_res(self.status_ref[0], 200, token.decode('utf-8')))
            return Response(gen_res(self.status_ref[1], 400, detail=self.error_ref[4]), status=400)
        return Response(gen_res(self.status_ref[1], 400, detail=self.error_ref[4]), status=400)


class AccountInfoView(generics.ListAPIView):
    authentication_classes = [AccountAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = AccountInfoSerializer(request.user)
        return res_by_gzip(gen_res('success', 200, dict(serializer.data)))
