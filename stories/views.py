from django.shortcuts import render
from django.views import generic
from .models import Story, Headline


class StoryList(generic.ListView):
    model = Story
    queryset = Story.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'
    paginate_by = 6


class HeadlineList(generic.ListView):
    model = Headline
    queryset = Headline.objects.filter(displayed=True).order_by('-created')
    template_name = 'index.html'
