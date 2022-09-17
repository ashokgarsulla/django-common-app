from django.shortcuts import render,HttpResponse

# Create your views here.
def setsession(request):
    # request.session.set_test_cookie()
    request.session["name"] = "Ashok Kumar"
    request.session.set_expiry(30)
    return render(request,'app/setsession.html')

def getsession(request):
    # name = request.session["name"]
    if "name" in request.session:
        name = request.session.get("name", default ="Not Set")
        return render(request,'app/getsession.html',{"name":name})
    else:
        return HttpResponse("Your page is expired")
    

def delsession(request):
    #  delete data from session
    # if "name" in request.session:
    #     del request.session["name"]
    # if request.session.test_cookie_worked():
    #     request.session.delete_test_cookie()
    # request.session.flush()
    # request.session.clear_expired()
    request.session.clear()
    return render(request,'app/delsession.html')
    