from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, "core/index.html")

def register(req):
    return render(req, 'registration/register.html')