from django.shortcuts import render

test = [
    {
        'title':'First Title',
        'Content' : 'First content try'
    },
    {
        'title':'Second Title',
        'Content' : 'Second content try'
    }
]

def home(request):
    cont = {
        'test' : test
    }
    return render(request , 'blog/home.html' , cont)

def about(request):
    return render(request , 'blog/about.html' , {'title': 'About'})