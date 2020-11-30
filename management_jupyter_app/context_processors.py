from .models import Category, Tag


def common(request):
    """テンプレートに毎回渡すデータ"""
    context = {
        "category_list": Category.objects.all(),
        'tag_list': Tag.objects.all()
    }

    return context
