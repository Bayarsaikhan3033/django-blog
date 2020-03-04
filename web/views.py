from django.shortcuts import render
from .models import Post, Comment
def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "index.html", context)