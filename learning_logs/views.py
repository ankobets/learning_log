from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForms, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def check_owner(request,topic_ow):
    if topic_ow.owner != request.user:
        raise  Http404


# Create your views here.

def index(request):
    return render(request, "learning_logs/index.html")


@login_required()
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required()
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_owner(request, topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required()
def new_topic(request):
    if request.method != 'POST':
        form = TopicForms()

    else:
        form = TopicForms(data=request.POST)

        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required()
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_owner(request, topic)

    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()

            return redirect('learning_logs:topic', topic_id=topic_id)
    else:
        form = EntryForm()

    return render(request, 'learning_logs/new_entry.html', {'topic': topic, 'form': form})


@login_required()
def edit_entry(request, entry_id):

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_owner(request, topic)

    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid:
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    else:
        form = EntryForm(instance=entry)

    context = {'entry': entry, 'topic':topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)






