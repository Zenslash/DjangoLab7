from django.shortcuts import render

def index(request):
  return render(request, "index.html")

def login(request):
  return render(request, "login.html")

def gallery(request):
  return render(request, "gallery.html")

def aboutUs(request):
  return render(request, "aboutUs.html")