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


class CategoryView(generic.ListView):
    model = Management
    paginate_by = 10

    def get_queryset(self):
        """
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Post.objects.order_by('-created_at').filter(category=category)
        """
        category_pk = self.kwargs['pk']
        queryset = Management.objects.order_by('-created_at').filter(category__pk=category_pk)

        return queryset


class TagView(generic.ListView):
    model = Management

    def get_queryset(self):
        """
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Post.objects.order_by('-created_at').filter(category=category)
        """
        tag_pk = self.kwargs['pk']
        queryset = Management.objects.order_by('-created_at').filter(tag__pk=tag_pk)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_key'] = self.kwargs['pk']
        return context

class CreateView(generic.CreateView):
    """アップロード画面"""
    model = Management
    form_class = ManagementCreateForm
    success_url = reverse_lazy('management_jupyter_app:index')


class PlayView(generic.DetailView):
    """詳細ページ"""
    model = Management
