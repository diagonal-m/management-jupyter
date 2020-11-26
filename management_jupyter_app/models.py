"""
データベースに定義したいデータを記述するファイル
"""
from django.db import models


class Management(models.Model):
    """
    htmlアップロード
    """
    title = models.CharField('タイトル', max_length=255)
    description = models.TextField('説明')
    # ファイルのパスがDBに保存される
    upload = models.FileField('htmlファイル', upload_to='uploads/%Y/%m/%d/')  # /media/uploads/2018/3/20/ファイル名
    created_at = models.DateTimeField('作成日', auto_now_add=True)  # default=timezone.nowと違い、入力欄は表示されない
    updated_at = models.DateTimeField('更新日', auto_now=True)  # 更新するたびにその日時が格納される

    def __str__(self):
        return self.title
