from django.shortcuts import render
from .models import Proj
from django.views.generic import ListView, DetailView

# Create your views here.
# def list(request):
#     data = {'posts': Post.objects.all().order_by("-date")}
#     return render(request, 'blog/blog.html', data)

class ProjListView(ListView):
    queryset = Proj.objects.all().order_by("-date")
    template_name = 'project/project.html'
    context_object_name = 'projs'
    paginate_by = 6
    
def content(request, id):
    proj = Proj.objects.get(id = id)
    return render(request, 'project/content.html', {'projs':proj})

