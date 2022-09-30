from django.shortcuts import render, redirect
from .models import Articles
import math

# Create your views here.
def index(request, num):
    title = Articles.objects.order_by('-updated_at')[(num-1)*15:num*15]
    btn = math.ceil(Articles.objects.all().count()/15)
    result = []
    for i in range(1, btn + 1):
        result.append(i)
    context = {
        'titles':title,
        'numbers':result,
    }
    return render(request, 'pairs/index.html', context)
def create(request):
    return render(request, 'pairs/create.html')
def create2(request):
    info = request.GET
    Articles.objects.create(title=info['title'], content=info['content'], user_name=info['name'], password=info['password'])
    return redirect('pairs:index', 1)
def detail(request, pk):
    id = Articles.objects.get(pk=pk)
    context = {
        'id': id,
    }
    return render(request, 'pairs/detail.html', context)
def edit(request, pk):
    id = Articles.objects.get(pk=pk)
    context = {
        'id': id,
    }
    return render(request, 'pairs/edit.html', context)
def edit2(request, pk):
    id = Articles.objects.get(pk=pk)
    edit = request.GET
    id.title = edit['title']
    id.content = edit['content']
    id.save()
    return redirect('pairs:index', 1)
def delete(request, pk):
    id = Articles.objects.get(pk=pk)
    id.delete()
    return redirect('pairs:index', 1)

def search(request, num):
    id = request.GET
    title = Articles.objects.order_by('-updated_at')[(num-1)*15:num*15]
    btn = math.ceil(Articles.objects.all().count()/15)
    result = []
    for i in range(1, btn + 1):
        result.append(i)
    context = {
        'titles':title,
        'numbers':result,
    }
    return render(request, 'pairs/search.html', context)