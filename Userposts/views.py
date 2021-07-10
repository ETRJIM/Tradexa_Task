from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from Userposts.models import Posts
from Userposts.forms import PostForm,SignUpForm
from django.utils import timezone
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
class PostsListView(ListView):
    model = Posts

    def get_queryset(self):
        return Posts.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')

class PostsDetailView(DetailView):
    model = Posts
    template_name='Userposts/posts_detail.html'


class PostsCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'Userposts/posts_detail.html'
    form_class = PostForm
    success_url = reverse_lazy('posts_list')
    model = Posts
    def form_valid(self,form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return HttpResponseRedirect(self.success_url)

class PostsUpdateView(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'Userposts/Posts_list.html'
    form_class = PostForm
    model = Posts
    success_url = reverse_lazy('posts_list')
    login_url = '/login/'
    def form_valid(self,form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return HttpResponseRedirect(self.success_url)

    

class PostsDeleteView(LoginRequiredMixin,DeleteView):
    model = Posts
    success_url = reverse_lazy('posts_list')

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'