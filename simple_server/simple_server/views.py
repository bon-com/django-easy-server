from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    """単純に文字列をレスポンスする"""
    return HttpResponse("Hello World")


def index_json(request):
    """JSON文字列でレスポンスする"""
    data = dict(id=1, name="ヤマダ", mail="xxx@gmail.xxx", nums=[1, 2, 3, 4])
    # json_dumps_params={'ensure_ascii': False}とすることで、日本語のUnicodeエスケープを回避する
    return JsonResponse(data, json_dumps_params={"ensure_ascii": False})


def index_html(request):
    """htmlでレスポンスする"""
    ctx = {"name": "ヤマダ"}
    return render(request, "index.html", ctx)
