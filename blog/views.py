from django.shortcuts import render
from blog.models import Post
# Create your views here.
def blog_home(request):
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    return render(request, 'blog/blog-single.html')

def test(request):
    posts = Post.objects.filter(status=True)
    context = {'posts':posts}
    return render(request, 'test.html', context)