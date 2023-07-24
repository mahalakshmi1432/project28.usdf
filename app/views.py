from django.shortcuts import render

# Create your views here.
def usdf(request):
    d={'data':'HELLO MaHALaKSHMI hOw aRE U WHATS gOInG ON'}
    return render(request,'usdf.html',d)