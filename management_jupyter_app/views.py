from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from .forms import ManagementCreateForm
from .models import Management


class IndexView(generic.ListView):
    """トップページ"""
    model = Management
    paginate_by = 10

    def get_queryset(self):
        """
        上書き(並び替え)
        """
        queryset = Management.objects.order_by('-created_at')  # created_atを元に並び替え
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(description__icontains=keyword)
            )

        return queryset


class CreateView(generic.CreateView):
    """アップロード画面"""
    model = Management
    form_class = ManagementCreateForm
    success_url = reverse_lazy('management_jupyter_app:index')


class PlayView(generic.DetailView):
    """詳細ページ"""
    model = Management
