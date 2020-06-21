
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomerForm


def home(request):

    
    return render(request,'home.html')

def uploaded_csv(request):
    return render(request,'uploaded.html')

def upload(request):
    if request.method =='POST':

     form = CustomerForm(request.POST, request.FILES)
     if form.is_valid():
         form.save()
         return(redirect('uploaded_csv')
     else:
         form =CustomerForm()
    return render(request, 'upload.html',{
        'form' : form
    })

