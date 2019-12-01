from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse

from rest_framework import generics

from api.account.models import Login
from api.account.serializers import RegisterAccountSerializer
from api.services.gzip_service import res_by_gzip


def defaultView(request):
    response = {
        'name': 'Hằng',
        'properties': 'Quí'
    }
    return res_by_gzip(response)


def dataView(request):
    response = {
        'data': 'Hằng cute',
        'status': 'active'
    }
    return res_by_gzip(response)


class RegisterAccountView(generics.CreateAPIView):
    queryset = Login.objects.all()
    serializer_class = RegisterAccountSerializer

    def create(self, request):
        response = {
            'name': 'Hằng',
            'properties': 'Quí'
        }
        return res_by_gzip(response)
