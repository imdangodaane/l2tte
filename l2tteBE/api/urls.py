from django.contrib import admin
from django.urls import path, include
from .views import defaultView, dataView
from api.account import views as account_views
from api.download import views as download_views


urlpatterns = [
    path('', defaultView),
    path('data', dataView),
    path('register', account_views.RegisterAccountView.as_view()),
    path('login', account_views.LoginCheckView.as_view()),
    path('download/<str:link_type>', download_views.DownloadLinkView.as_view()),
    path('account/information', account_views.AccountInfoView.as_view()),
]
