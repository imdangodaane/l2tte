from rest_framework import generics
from rest_framework.response import Response

from django.forms.models import model_to_dict

from api.download.models import DownloadLinkModel
from api.download.serializers import DownloadLinkSerializer
from api.services.gzip_service import res_by_gzip
from api.services.response_service import gen_res


class DownloadLinkView(generics.RetrieveUpdateAPIView):
    queryset = DownloadLinkModel
    serializer_class = DownloadLinkSerializer

    def get(self, request, link_type, *args, **kwargs):
        instance = DownloadLinkModel.objects.get(pk=1)
        if link_type == 'link-patch':
            res_data = instance.link_patch
        else:
            res_data = instance.link_full
        return res_by_gzip(gen_res('success', 200, res_data, link_type))

    def put(self, request, link_type, *args, **kwargs):
        instance = DownloadLinkModel.objects.get(pk=1)
        payload = request.data.copy()
        if link_type == 'link-full':
            try:
                DownloadLinkModel.objects.filter(pk=1).update(link_full=payload['link_full'])
            except KeyError:
                return Response(gen_res('fail', 400, {}, 'update link_full fail'))
        elif link_type == 'link-patch':
            try:
                DownloadLinkModel.objects.filter(pk=1).update(link_patch=payload['link_patch'])
            except KeyError:
                return Response(gen_res('fail', 400, {}, 'update link_patch fail'))
        response_data = {
            'link_full': instance.link_full,
            'link_patch': instance.link_patch
        }
        return res_by_gzip(gen_res('success', 200, response_data, 'update success'))

    def patch(self, request, link_type, *args, **kwargs):
        instance = DownloadLinkModel.objects.get(pk=1)
        payload = request.data.copy()
        if link_type == 'link-full':
            try:
                DownloadLinkModel.objects.filter(pk=1).update(link_full=payload['link_full'])
            except KeyError:
                return Response(gen_res('fail', 400, {}, 'update link_full fail'))
        elif link_type == 'link-patch':
            try:
                DownloadLinkModel.objects.filter(pk=1).update(link_patch=payload['link_patch'])
            except KeyError:
                return Response(gen_res('fail', 400, {}, 'update link_patch fail'))
        response_data = {
            'link_full': instance.link_full,
            'link_patch': instance.link_patch
        }
        return res_by_gzip(gen_res('success', 200, response_data, 'update success'))
