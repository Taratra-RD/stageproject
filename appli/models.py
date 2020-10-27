from django.db import models 

class MyModel(models.Model): 
  
    
    title = models.CharField(max_length = 200) 
    description = models.TextField(blank=True, default='') 
  
   
    def __str__(self): 
        return self.title
