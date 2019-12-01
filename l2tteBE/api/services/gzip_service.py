import gzip
import json
from django.middleware.gzip import GZipMiddleware
from django.http import HttpResponse

gzip_middleware = GZipMiddleware()


def data_to_gzip(data):
    file_name = 'gz-warehouse/items.gz'
    with gzip.GzipFile(file_name, 'w') as fout:
        fout.write(json.dumps(data).encode('utf-8'))
    return file_name


def res_by_gzip(data):
    gzip_file_name = data_to_gzip(data)
    response = HttpResponse(open(gzip_file_name, 'rb'))
    response['Content-Encoding'] = 'gzip'
    return response
