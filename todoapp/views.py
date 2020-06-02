from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Todo,Profile
from .forms import RegistrationForm, TodoForm, TodoEditForm, ProfileForm



class HomeView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'dashboard.html'


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, self.template_name, {'form':form})

class TodoAllView(LoginRequiredMixin, ListView):
    model=Todo
    template_name='todoes/todo_list.html'

class DetailTodoView(DetailView):
    model = Todo
    template_name = 'todoes/todo_detail.html'


class TodoEditView(LoginRequiredMixin, TemplateView):
    template_name = 'todoes/todo_edit.html'
    id = None

    def get(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
            form = TodoEditForm(instance=todo)
            return render(request, self.template_name, {'form':form, 'todo':todo})
        except Exception as error:
            messages.error(request, error)
            return HttpResponseRedirect(reverse('todo-detail'))

    def post(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
            form = TodoEditForm(request.POST, instance=todo)
            if form.is_valid():
                updated_todo = form.save()
                user = form.cleaned_data.get('user')
                photo = form.cleaned_data.get('photo')
                bio = form.cleaned_data.get('bio')
                messages.success(request, "Post successfully updated")
                return HttpResponseRedirect(reverse('todo-detail'))
            else:
                messages.error(request, "Please correct your input")
                return render(request, self.template_name, {'form':form, 'todo':todo} )
        except Exception as error:
                messages.error(request, error)
                return render(request, self.template_name, {'form':form, 'todo':todo} )

class TodoCreateView(LoginRequiredMixin ,TemplateView):
    template_name = 'todoes/todo_create.html'

    def get(self, request):
        form = TodoEditForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = TodoEditForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Yeay To-do successfully added")
            return HttpResponseRedirect(reverse('todo-detail'))
        else:
            messages.error(request, "Please correct your input")
            return render(request, self.template_name, {'form':form})

class ProfileView(TemplateView):
    template_name = 'profiles/profile.html'

    def get(self, request):
        return render(request, self.template_name)


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    templat_ename = 'profiles/profile-edit.html'
    id = None

    def get(self, request, id):
        try:
            profile = Profile.objects.get(id=id)
            form = ProfileForm(instance=profile)
            return render(request, self.template_name, {'form':form, 'profile':profile})
        except Exception as error:
            messages.error(request, error)
            return HttpResponseRedirect(reverse('profile'))

    def post(self, request, id):
        try:
            profile = Profile.objects.get(id=id)
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                updated_profile = form.save()
                messages.success(request, "Your Profile successfully updated")
                return HttpResponseRedirect(reverse('profile'))
            else:
                messages.error(request, "Please correct your input")
                return render(request, self.template_name, {'form':form, 'profile':profile} )
        except Exception as error:
                messages.error(request, error)
                return render(request, self.template_name, {'form':form, 'profile':profile} )