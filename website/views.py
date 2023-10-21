from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    context = {'name': 'Soheil', 'lastName': 'Elahifar ', 'email': 'l.o0of.war@gmail.com', 'phoneNumber': '+989385818676'}
    return render(request, 'website/index.html', context)

def pDetail_view(request):
    return render(request, 'website/portfolio-details.html')