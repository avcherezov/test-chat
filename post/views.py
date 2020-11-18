from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Message
from .forms import MessageForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        chat_user = User.objects.filter(username__exact=search_query).exclude(username=request.user)
        if not chat_user:
            return render(request, 'no_user.html')
    else:
        chat_user = User.objects.all().exclude(username=request.user)
    return render(request, 'index.html', {'chat_user': chat_user})


@login_required
def chat(request, username):
    chat = User.objects.get(username=username)
    messages = Message.objects.filter(Q(recipient__username=username, sender__username=request.user) | Q(recipient__username=request.user, sender__username=username))
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = chat
            message.save()
            return redirect('chat', username)
    else:
        form = MessageForm()
    return render(request, 'chat.html', {'messages': messages, 'chat': chat, 'form': form})


@login_required
def add_message(request, username):
    recipient = User.objects.get(username=username)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect('chat', username)
    else:
        form = MessageForm()
    return render(request, "message.html", {"form": form})