from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def main(request):
    return request(request, 'main.html')


def introduction(request):
    return render(request, 'introduction.html')
