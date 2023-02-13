from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from applist.forms import TaskForm
from applist import models
from .models import ModelClass
from django.views.generic import UpdateView,ListView

# Create your views here.

def add_fun(request):
    all_task=models.ModelClass.objects.all()
    if request.POST:
        
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('applist:add'))
    else:
        form=TaskForm()
        return render(request,'applist/add.html',context={'form':form,'all_task':all_task})
    
def delete_fun(request,i):
    item=models.ModelClass.objects.get(id=i)
    item.delete()
    return redirect('applist:add')

class Update_form(UpdateView):
    template_name='applist/add.html'
    model=ModelClass
    fields='__all__'
    success_url=reverse_lazy('applist:add')
    
class Update_List(ListView):
    model=ModelClass
    template_name='applist/update_list.html'
    content_object_name='object_list'
    


    