from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
# def list(request):
#     data = {'posts': Post.objects.all().order_by("-date")}
#     return render(request, 'blog/blog.html', data)

class PostListView(ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 1
    
def post(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'blog/post.html', {'post':post})

