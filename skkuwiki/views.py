from django.shortcuts import render


def home(request):
    print("qwe")
    return render(request, './home.html')
