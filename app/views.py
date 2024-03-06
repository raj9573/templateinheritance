from django.shortcuts import render

# Create your views here.


def base(request):

    return render(request,'base.html')

    

def first(request):

    return render(request,'first.html')