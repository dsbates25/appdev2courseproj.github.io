from django.urls import path
import todolist.views

urlpatterns = [path("", todolist.views.index, name="index"), 
]




