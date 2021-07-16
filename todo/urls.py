from django.urls import path
from . import views

app_name='todo'

urlpatterns = [
    #todo
    # list view
    path('todo_list', views.TodoListView.as_view(),
         name='todo_list'),
    # detail views
    path('todo_detail/<int:pk>', views.TodoDetailView.as_view(),
         name='todo_detail'),
    # CRUD
    # Create
    path('todo_create', views.TodoCreateView.as_view(),
         name='todo_create'),
    # Update
    path('todo_update/<int:pk>', views.TodoUpdateView.as_view(),
         name='todo_update'),
    # Delete
    path('todo_delete/<int:pk>', views.TodoDeleteView.as_view(),
         name='todo_delete'),

]