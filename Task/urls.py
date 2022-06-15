from django.urls import path
from .views import *

urlpatterns = [
    path('addTodo/', addTodo, name="addTodo"),
    path('deleteTodo/<int:id>', deleteTodo, name="deleteTodo"),
    # path('test/', test, name="test")
]