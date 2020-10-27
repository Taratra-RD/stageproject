from django.shortcuts import render
from django.http import HttpResponse 
from django.views import View 
from django.views.generic.edit import (CreateView,UpdateView,DeleteView,FormView)
from django.views.generic import (ListView,DetailView)
from .models import MyModel 
  
class MyView(View): 
    def get(self, request): 
        return HttpResponse('result') 

class GeeksCreate(CreateView): 
  
    model = MyModel  
    fields = ['title', 'description'] 
    success_url ="http://localhost:8000/appli/list"


class GeeksList(ListView): 
  
    model = MyModel

class GeeksUpdateView(UpdateView): 

    model = MyModel 
  
    fields = [ 
        "title", 
        "description"
    ] 
    success_url ="http://localhost:8000/appli/create"

class GeeksDeleteView(DeleteView): 
    
    model = MyModel 
      
    success_url ="http://localhost:8000/appli/list"

  
class GeeksDetailView(DetailView): 
    
    model = MyModel 