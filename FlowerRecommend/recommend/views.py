from django.shortcuts import render

# Create your views here.


def recom(request):
    return render(request, "flower.html")
