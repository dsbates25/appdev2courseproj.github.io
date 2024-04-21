from django.shortcuts import render



def index(request): 
    return render(request,"todolist/index.html")

def currentlyWatching(request): 
    context = {}
    return render(request,"todolist/currentlyWatching.html")

def recommendations(request): 
    context = {}
    return render(request,"todolist/recommendations.html")

def login(request): 
    context = {}
    return render(request,"todolist/login.html")


