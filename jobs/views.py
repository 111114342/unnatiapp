from django.shortcuts import render,HttpResponseRedirect
from .models import Job
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Function based and Class Bsed View
#
# def home(request):
#     jobs = Job.objects
#     return render(request, 'jobs/home.html', {'jobs': jobs})

class JobHome(ListView):
    model = Job
    context_object_name = 'exps' # context_object_name = 'objects_list':
    template_name = 'jobs/home.html'


@method_decorator(login_required, name='dispatch')
class CreateAchieve(CreateView):
    model = Job
    fields = '__all__'
    template_name = 'jobs/createachieve.html'



    def get_success_url(self):
        return reverse ('achievement_page')
class UpdateAchieve(UpdateView):
    model = Job
    fields = '__all__'
    template_name = 'jobs/updateachieve.html'
    def get_success_url(self):
        return reverse('achievement_page')
def job_delete_view(request,id):
    mydict = {'msg':'job Data Deleted'}
    del_student = Job.objects.get(id=id)
    del_student.delete()
    del_student = Job.objects.all()
    return HttpResponseRedirect('')
