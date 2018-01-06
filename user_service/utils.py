from rest_framework.views import exception_handler
import traceback
from django.http import JsonResponse
from django.http import HttpResponse
import json

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        response.data['error'] = response.data['detail']
        del response.data['detail']

    return response
'''
class CustomExceptionHandler:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        print(request)
        return JsonResponse({'error' : str(exception)})
'''
