from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def riot(request):
    return render(request, "index-riot.html")

def riotpug(request):
    return render(request, "index-riot-pug.html")

def vue(request):
    return render(request, "index-vue.html")