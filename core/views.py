from django.shortcuts import render

def home(request):
    return render(request, '../templates/core/base.html')
def secondpage(request):
    return render(request, '../templates/core/secondpage.html')