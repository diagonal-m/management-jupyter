from django.urls import reverse_lazy
from django.views import generic
from .forms import ManagementCreateForm
from .models import Management


class IndexView(generic.ListView):
    """トップページ"""
    model = Management


class CreateView(generic.CreateView):
    """アップロード画面"""
    model = Management
    form_class = ManagementCreateForm
    success_url = reverse_lazy('management_jupyter_app:index')


class PlayView(generic.DetailView):
    """詳細ページ"""
    model = Management
