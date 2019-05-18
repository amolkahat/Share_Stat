from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "pages/home.html")

def login(request):
    if request.method == 'POST':
        userid = ''
        password = ''
        try:
            userid = request.POST['uname1']
            password = request.POST['pwd1']
            print(userid, password)
        except:
            print("Error..")

        if userid == 'janedone' and password == 'Secret123':
            return render(request, 'pages/home.html')
    return render(request, "pages/login.html")

def signup(request):
    return render(request, "pages/signup.html")

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")
