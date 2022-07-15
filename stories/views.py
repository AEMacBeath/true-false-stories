from django.shortcuts import render
from django.views import generic
from .models import Story


class StoryList(generic.ListView):
    model = Story
    gueryset = Story.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'
    paginate_by = 5
