"""missing"""
from django.db.models import Count, Q
from django.shortcuts import render
#from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView

#from django.views.generic import ListView
from . import models


class HomeView(TemplateView):
    """Missing"""
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        # Get the parent context
        context = super().get_context_data(**kwargs)

        latest_posts = models.Post.objects.published() \
            .order_by('-published')[:3]
        # Update the context with our context variables
        context.update({
            #'authors': authors,
            'latest_posts': latest_posts
            #'Topics': models.Post.objects.get_topics()
        })

        return context
class AboutView(TemplateView):
    """Missing"""
    def get(self, request):
        return render(request, 'blog/about.html')
class AboutView(TemplateView):
    """Missing"""
    template_name = 'blog/about.html'
    def get_context_data(self, **kwargs):
        # Get the context from the parent class
        context = super().get_context_data(**kwargs)

        # Define the "authors" context variable
        context['authors'] = models.Post.objects.published() \
            .get_authors() \
            .order_by('first_name')
        context['topics'] = models.Topic.objects.all().annotate(num_posts= Count('blog_posts'))\
            .order_by('-num_posts')
        return context
def terms_and_conditions(request):
    """Missing"""
    return render(request, 'blog/terms_and_conditions.html')
class PostListView(ListView):
    """Missing"""
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects.published().order_by('-published')# Customized queryset
class PostDetailView(DetailView):
    """Missing"""
    model = models.Post

    def get_queryset(self):
        # Get the base queryset
        queryset = super().get_queryset().published()

        # If this is a `pk` lookup, use default queryset
        if 'pk' in self.kwargs:
            return queryset

        # Otherwise, filter on the published date
        return queryset.filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )
    def get_context_data(self, **kwargs):
        # Get the context from the parent class
        context = super().get_context_data(**kwargs)

        context['topics'] = models.Topic.objects.all().filter(blog_posts__id=context['object'].id)
        return context
class TopicListView(ListView):
    """Missing"""
    model = models.Topic
    context_object_name = 'topics'
    queryset=models.Topic.objects.all().annotate(num_posts= Count('blog_posts'))\
        .order_by('-num_posts')
    template_name= 'blog/topics_list.html'
class TopicDetailView(DetailView):
    """Missing"""
    model = models.Topic
    def get_context_data(self, **kwargs):
        # Get the context from the parent class
        context = super().get_context_data(**kwargs)
        context['posts'] = models.Post.objects.all().filter(topics__id=context['object'].id, status=models.Post.PUBLISHED)
        return context
    def get_queryset(self):
        queryset=super().get_queryset().annotate(num_posts= Count('blog_posts'))\
            .order_by('-num_posts')
        return queryset
