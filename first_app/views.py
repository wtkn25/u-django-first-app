from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("hello")


def user_page(request, user_name):
    return HttpResponse(f"<h1>{user_name}'s page<h1>")


def number_page(request, number):
    return HttpResponse(f"<h1>page_number = {number}<h1>")
