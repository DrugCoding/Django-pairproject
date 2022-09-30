from django.urls import path
from pairs import views

app_name = 'pairs'

urlpatterns = [
    path('index/<int:num>', views.index, name='index'),

]