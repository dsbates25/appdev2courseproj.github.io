from django.shortcuts import render



def index(request): 
    return render(request,"todolist/index.html")

def testuserpage(request): 
    context = {}
    return render(request,"todolist/testuserpage.html")


def login(request): 
    context = {}
    return render(request,"todolist/login.html")


