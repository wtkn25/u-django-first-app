import logging

from django.http import HttpResponse
from django.shortcuts import render

application_logger = logging.getLogger("application-logger")
error_logger = logging.getLogger("error-logger")


def index(request):
    application_logger.debug("メッセージ")
    return HttpResponse("hello")


def user_page(request, user_name):
    application_logger.info("メッセージ")
    return HttpResponse(f"<h1>{user_name}'s page<h1>")


def number_page(request, number):
    return HttpResponse(f"<h1>page_number = {number}<h1>")


# エラーログを検証するための関数
def error_func(request):
    from django.http import Http404

    if "aaa" != "bbb":
        error_logger.error("aaaとbbbは一致しません")
        raise Http404("このページは存在しません")
