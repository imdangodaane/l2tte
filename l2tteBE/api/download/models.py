from django.db import models


class DownloadLinkModel(models.Model):
    link_full = models.TextField(default='', blank=True, null=True)
    link_patch = models.TextField(default='', blank=True, null=True)
