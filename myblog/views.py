from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {"page":"Home"})

def about(request):
	return render(request, 'about.html', {"page":"About"})