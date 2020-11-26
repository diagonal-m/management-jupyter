from django.urls import path
from . import views

app_name = 'management_jupyter_app'

urlpatterns = [
    # e.g.) http://localhost:8001/のときはviewsのIndexViewクラスを指定する
    path('', views.IndexView.as_view(), name='index'),
    # e.g.) http://localhost:8001/upload/のときはviewsのCreateViewクラスを指定する
    path('upload/', views.CreateView.as_view(), name='upload'),
    # e.g.) http://localhost:8001/article/3のときはviewsのCreateViewクラスを指定する
    path('article/<int:pk>/', views.PlayView.as_view(), name='article'),
]
