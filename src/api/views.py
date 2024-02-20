from django.http import JsonResponse

# Create your views here.

def get_response(request):
    return JsonResponse({
        "blogs" : ["Cara Mengubah Code Menjadi Uang", "Python, Anaconda, Cobra Merupakan Nama Jenis Ular"]
    })