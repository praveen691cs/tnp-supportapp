from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def link1(request):
    return render(request, 'link1.html')
def link2(request):
    return render(request, 'link2.html')
def link3(request):
    return render(request, 'link3.html')
def link4(request):
    return render(request, 'link4.html')
def link5(request):
    return render(request, 'link5.html')