from django.shortcuts import render


# Create your views here.
def base(request):
    context = {
        "blogs" : ["Cara Mengubah Code Menjadi Uang", "Python, Anaconda, Cobra Merupakan Nama Jenis Ular"]
    }
    return render(request, "blog/index.html", context)
