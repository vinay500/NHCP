import logging

class ExceptionLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('exception_logger')

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        # Log the exception with traceback
        self.logger.error("Exception occurred", exc_info=True)
        # Return None to allow Django's default exception handling to take over
        return None
