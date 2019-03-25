from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import AddForm

def index(request):
    return render(request,'home.html')
def manhua(request):
    return render(request,'manhua.html')
def manhua_douluodalu(request):
    return render(request,'manhua/douluodalu.html')
def face_recognition(request):
    # if request.method=='POST':
    #     form=AddForm(request.POST)
    # form=AddForm()
    return render(request,'face.html')