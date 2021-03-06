"""
データベースに定義したいデータを記述するファイル
"""
from django.db import models


class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    Tagモデル
    """
    name = models.CharField('タグ', max_length=50)

    def __str__(self):
        return self.name


class Management(models.Model):
    """
    htmlアップロード
    """
    title = models.CharField('タイトル', max_length=255)
    description = models.TextField('説明')
    # ファイルのパスがDBに保存される
    upload = models.FileField('HTMLファイル', upload_to='uploads/%Y/%m/%d/')  # /media/uploads/2018/3/20/ファイル名
    created_at = models.DateTimeField('作成日', auto_now_add=True)  # default=timezone.nowと違い、入力欄は表示されない
    updated_at = models.DateTimeField('更新日', auto_now=True)  # 更新するたびにその日時が格納される

    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
    )
    tag = models.ManyToManyField(Tag, verbose_name='タグ')

    def __str__(self):
        return self.title
