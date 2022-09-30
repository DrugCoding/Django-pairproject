from multiprocessing import context
from turtle import title
from unittest import result
from django.shortcuts import render
from .models import Articles
import math

# Create your views here.
def index(request, num):

    title = Articles.objects.order_by('updated_at')[(num-1)*15:num*15]
    btn = math.ceil(Articles.objects.all().count()/15)
    result = []
    for i in range(1, btn + 1):
        result.append(i)
    context = {
        'titles':title,
        'numbers':result,
    }

    return render(request, 'pairs/index.html', context)

