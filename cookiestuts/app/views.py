from urllib import response
from django.shortcuts import render,HttpResponse

# Create your views here.
def setcookies(request):
    response = render(request,'app/setcookies.html')
    response.set_cookie('name','ashok kumar',max_age=60)
    return response

def delcookies(request):
    response = render(request,'app/delcookies.html')
    response.delete_cookie('name')
    return response

def getcookies(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get("name","guest")
    return render(request,'app/getcookies.html',{"name":name})
    