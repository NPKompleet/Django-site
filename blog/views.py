from django.shortcuts import render, get_object_or_404
from .models import Post, Quote, Project

def post_list(request):
	posts= Post.objects.all()
	return render(request, 'post_list.html', {'posts':posts, "page":"Blog"})


def post_detail(request, pk):
	post=get_object_or_404(Post, pk=pk)
	return render(request, 'blog_detail.html', {'post':post, "page":"Blogpost"})



def quote_list(request):
	quotes= Quote.objects.all()
	return render(request, 'quote_list.html', {'quotes': quotes, "page":"Quote"})


def project_list(request):
	projects= Project.objects.all()
	return render(request, 'project_list.html', {'projects': projects, "page":"Project"})
