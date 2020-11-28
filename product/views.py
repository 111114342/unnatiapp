from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
from product.models import Product
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/product.html'

# @method_decorator(login_required, name='dispatch')
class CreateProduct(CreateView):
    model = Product
    fields = ['title', 'image', 'body']
    template_name = 'product/createproduct.html'

    def get_success_url(self):
        return reverse ('product_list_view')
class UpdateProduct(UpdateView):
    model = Product
    fields=['title','image','body']
    template_name = 'product/updateproduct.html'
    def get_success_url(self):
        return reverse('product_list_view')

def product_delete_view(request,id):
    mydict = {'msg':'Product Data Deleted'}
    del_student = Product.objects.get(id=id)
    del_student.delete()
    del_student = Product.objects.all()
    return HttpResponseRedirect("/product/")
