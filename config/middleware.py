import logging
import time

from django.http import HttpRequest
from django.http.response import HttpResponse
from django.utils.deprecation import MiddlewareMixin

application_logger = logging.getLogger("application-logger")
error_logger = logging.getLogger("error-logger")
performance_logger = logging.getLogger("performance-logger")


class MyMiddleware(MiddlewareMixin):
    # viewを呼び出す前に実行される
    def process_view(self, request: HttpRequest, view_func, view_args, view_kwargs):
        application_logger.info(request.get_full_path())

    # 例外発生時に実行される
    def process_exception(self, request, exception):
        error_logger.error(exception, exc_info=True)


class PerformanceMiddleware(MiddlewareMixin):
    # process_responseに合わせて、process_requestでもよかったかも？
    # https://docs.djangoproject.com/en/3.2/topics/http/middleware/#dealing-with-streaming-responses
    def process_view(self, request: HttpRequest, view_func, view_args, view_kwargs):
        start_time = time.time()

        request.start_time = start_time

    # レスポンスを返す際に実行される。テンプレートを返すときじゃないと実行されないみたいので注意
    # def process_template_response(self, request: HttpRequest, response: HttpResponse):
    # こっちは普通にresponseを返すときに使えそう。
    def process_response(self, request: HttpRequest, response: HttpResponse):
        response_time = time.time() - request.start_time
        performance_logger.info(f"{request.get_full_path()}: {response_time}s")
        return response
