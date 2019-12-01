from api.account.models import Login, Token
from rest_framework import authentication
from rest_framework import exceptions
import jwt


with open('./assets/jwt-key.pub') as f:
    public_key = f.read()


class AccountAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        http_authorization = request.META.get('HTTP_AUTHORIZATION')
        if not http_authorization:
            print('Without Token!!')
            return None

        try:
            token_type = http_authorization.split()[0]
            token = http_authorization.split()[1]
            if token_type == 'Bearer':
                data = jwt.decode(token, public_key, algorithms=['RS256'])
                user = Login.objects.get(pk=data['id'])
            else:
                raise exceptions.AuthenticationFailed('token type not support')
        except (Login.DoesNotExist, jwt.exceptions.InvalidSignatureError):
            raise exceptions.AuthenticationFailed('auth-fail1')

        try:
            token_instance = Token.objects.get(user=user)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('auth-fail2')

        if not token_instance.token == token:
            raise exceptions.AuthenticationFailed('auth-fail3')

        return (user, token_instance)
