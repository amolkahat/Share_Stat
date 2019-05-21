from django.shortcuts import render
from django.http import HttpResponse
from .models import UserData
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

        if userid == 'janedoe' and password == 'Secret123':
            return render(request, 'pages/home.html')
    return render(request, "pages/login.html")

def signup(request):
    userid = ''
    email = ''
    password = ''
    if request.method == 'GET':
        return render(request, 'pages/signup.html')

    if request.method == 'POST':
        userid = request.POST['uname1']
        email = request.POST['email']
        password = request.POST['pwd1']
        confirm = request.POST['pwd2']

        if password == confirm:
            u_data = UserData()
            u_data.username = userid
            u_data.pasword = password
            u_data.email = email
            u_data.save()
        else:
            context = {'password_match': True,
                        'warning': 'Passwords do not mactch'}
            return render(request, 'pages/signup.html', context)

        return render(request, "pages/login.html")


def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")
