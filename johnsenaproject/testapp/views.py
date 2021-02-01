from django.shortcuts import render
def homefunc(request):
    return render(request,'testapp/home.html')
def profilefunc(request):
    return render(request,'testapp/profile.html')

# Create your views here.
