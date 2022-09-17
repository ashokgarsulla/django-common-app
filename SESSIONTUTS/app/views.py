from django.shortcuts import render

# Create your views here.
def setsession(request):
    # request.session.set_test_cookie()
    request.session["name"] = "Ashok Kumar"
    request.session.set_expiry(30)
    return render(request,'app/setsession.html')

def getsession(request):
    # name = request.session["name"]
    name = request.session.get("name", default ="Not Set")
    print("============GET=========")
    print(request.session.get_session_cookie_age())
    return render(request,'app/getsession.html',{"name":name})
    

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
    