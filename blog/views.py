from django.shortcuts import render, get_object_or_404
from blog.models import Post
# Create your views here.
def blog_home(request):
    posts = Post.objects.filter(status=True)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request):
    return render(request, 'blog/blog-single.html')

def test(request, pid):
    posts = get_object_or_404(Post, id=pid)
    context = {'posts':posts}
    return render(request, 'test.html', context)