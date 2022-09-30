from django.urls import path
from pairs import views

app_name = 'pairs'

urlpatterns = [
    path('index/<int:num>', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create2/', views.create2, name='create2'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('edit2/<int:pk>', views.edit2, name='edit2'),
]