from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from django_htmx.middleware import HtmxDetails

class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails
# Create your views here.
    
@require_GET
def index(request: HtmxHttpRequest) -> HttpResponse:
    context = {
        "blogs" : ["Cara Mengubah Code Menjadi Uang", "Python, Anaconda, Cobra Merupakan Nama Jenis Ular"],
    }
    return render(request, "blog/blog_list.html", context)