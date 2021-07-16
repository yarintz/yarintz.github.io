from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

# Create your views here.
class TodoListView(ListView):
    model=Todo

    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        try:
            my_todo_list = Todo.objects.filter(user=self.request.user)
            context['my_todo_list'] = my_todo_list
        except:
            pass

        return context


class TodoDetailView(DetailView):
    model=Todo

class TodoCreateView(LoginRequiredMixin, CreateView):
    model=Todo
    fields=['title', 'description', 'important']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'description', 'important']

    def get_object(self):
        todo = super(TodoUpdateView, self).get_object()
        if not todo.user == self.request.user:
            raise Http404('You dontt have permission to do this. go away you hacker')
        return todo


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:todo_list')

    def get_object(self):
        todo = super(TodoDeleteView, self).get_object()
        if not todo.user == self.request.user:
            raise Http404('You dontt have permission to do this. go away you hacker')
        return todo
