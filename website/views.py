from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    return render(request, 'website/index.html')

def pDetail_view(request):
    return render(request, 'website/portfolio-details.html')