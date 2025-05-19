from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    if request.GET.get("yr"):
        year=int(request.GET.get("yr"))
        res="Leap year" if year%4==0 else "Not a Leap year"
        msg=str(year)+" is "+str(res)
        return render(request,"home.html",{"msg":msg})
    else:
        return render(request,"home.html")
# Create your views here.
