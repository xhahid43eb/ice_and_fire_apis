from rest_framework.response import Response


def make_formatted_response(status_code, data=None, message=None, error=None):
    if error:
        formatted_response = {'status_code': status_code,
                              'status': '',
                              'error': error
                              }
    else:
        formatted_response = {'status_code': status_code,
                              'status': 'success',
                              'data': data or []
                              }
        if message is not None:
            formatted_response['message'] = message

    return Response(formatted_response, status=status_code)
