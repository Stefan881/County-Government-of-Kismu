from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def services(request):
    return render(request,'services.html',{})

def portfolio(request):
    return render(request,'portfolio.html',{})

def team(request):
    return render(request,'team.html',{})

def blog(request):
    return render(request,'blog.html',{})

def blogDetails(request):
    return render(request,'blog-details.html',{})


def contact(request):
    return render(request,'contact.html',{})


