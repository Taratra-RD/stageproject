from django.urls import path 
from .views import (MyView,GeeksDeleteView,GeeksUpdateView,GeeksList,GeeksCreate,GeeksDetailView)

urlpatterns = [
    path('about/', MyView.as_view(),name="view"), 
    path('create', GeeksCreate.as_view(),name="create"), 
    path('list', GeeksList.as_view(),name="list"), 
    path('<pk>/update/', GeeksUpdateView.as_view(),name="update"),
    path('delete/<pk>/', GeeksDeleteView.as_view(),name="delete"), 
    path('detail/<pk>/', GeeksDetailView.as_view(),name="detail"),
] 
