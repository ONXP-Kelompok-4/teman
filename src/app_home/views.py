from django.shortcuts import render


def home_view(request):
    return render(request, 'app_home/home.html')