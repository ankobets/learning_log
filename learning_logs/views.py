from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Topic, Entry
from .forms import TopicForms, EntryForm
from django.views.generic import CreateView


# Create your views here.

def index(request):
    return render(request, "learning_logs/index.html")


def topics(request):
    topics = Topic.objects.order_by("date_added")
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForms()

    else:
        form = TopicForms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()

            # Getting the current instance object to display in the template
            img_object = form.instance

            return redirect('learning_logs:topic', topic_id=topic_id)
    else:
        form = EntryForm()

    return render(request, 'learning_logs/new_entry.html', {'topic': topic, 'form': form})
