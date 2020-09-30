from time import time
from user.models import Logger


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        response = self.get_response(request)
        result_time = time() - start
        Logger.objects.create(
            method=request.method,
            path=request.path,
            response_time=result_time
        )

        return response
