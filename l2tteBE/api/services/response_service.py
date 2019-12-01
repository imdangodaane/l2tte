def gen_res(status='', status_code=404, data={}, detail=''):
    response = {
        'status': status,
        'status_code': status_code,
        'data': data,
        'detail': detail
    }
    return response
