from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "i am bold"}
    
    return render(request, 'fc_core/index.html', context_dict)

# Create your views here.
