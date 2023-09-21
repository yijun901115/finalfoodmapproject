from django.shortcuts import render


# Create your views here.


def navbarandbackground(request):
    return render(request, "thenavbarandbackground.html")


def homepage(request):
    return render(request, "homepage.html")

def aboutUs(request):
    return render(request, "aboutUs.html")
