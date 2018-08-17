from django.shortcuts import render, redirect
from .models import Message, comments
import re

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
# Create your views here.
def index(request):

    return render(request, "wall_app/index.html", {"messages":Message.objects.all()})

def add_message(request):
    Message.objects.create(text=request.POST['text'], user_name=request.POST['user'])
    return redirect("/")

def add_comment(request):
    comments.objects.create(text=request.POST['text'], user_name=request.POST['user'], color=request.POST['color'], messages=Message.objects.get(id=request.POST["messageId"]))
    return redirect("/")

def delete_message(request, m_id):
    Message.objects.filter(id=m_id).delete()
    return redirect("/")

def toEdit(request, m_id):
    return render(request, "wall_app/toEdit.html", {"message":Message.objects.get(id=m_id)})

def Edit(request, m_id):
    a = Message.objects.get(id=m_id)
    a.text = request.POST["text"]
    a.user_name = request.POST["user"]
    a.save()
    return redirect("/")