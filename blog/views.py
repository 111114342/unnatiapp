from django.shortcuts import render,get_object_or_404 ,redirect, HttpResponseRedirect
from .models import Blog
from django.views.generic import ListView, DetailView,UpdateView, DeleteView

from django.shortcuts import render

# Create your views here.
from product.models import Product
from django.views.generic import ListView,CreateView,UpdateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# def allblogs(request):
#     blogs = Blog.objects
#     return render(request, 'blog/allblogs.html', {'blogs': blogs})
# def detail(request,blog_id):
#      blogdetail=get_object_or_404(Blog, pk=blog_id)
#      return render(request, 'blog/detail.html', {'blog': blogdetail})

class BlogListView(ListView):
    model=Blog
    context_object_name = 'blogs'
    template_name ='blog/allblogs.html'

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog_details' # context_object_name = 'objects_list':
    template_name = 'blog/detail.html'


class CreateBlog(CreateView):
    model = Blog
    fields = ['title', 'image', 'body']
    template_name = 'blog/createblog.html'

    def get_success_url(self):
        return reverse ('blog_list_view')
class UpdateBlog(UpdateView):
    model = Blog
    fields = ['title','image','body']
    template_name ='blog/updateblog.html'
    def get_success_url(self):
        return reverse('blog_list_view')





#############################################################deleteblog with function based ############################3###############
def blog_delete_view(request,id):
    mydict = {'msg':'blog Data Deleted'}
    del_student = Blog.objects.get(id=id)
    del_student.delete()
    del_student = Blog.objects.all()
    return HttpResponseRedirect("/blog/")
