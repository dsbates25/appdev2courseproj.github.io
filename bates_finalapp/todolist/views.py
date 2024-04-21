from django.shortcuts import render



def index(request): 
    return render(request,"todolist/index.html")

def testuser(request): 
    context = {}
    return render(request,"todolist/testuser.html")


def login(request): 
    context = {}
    return render(request,"todolist/login.html")


