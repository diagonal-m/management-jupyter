# management-jupyter
勉強用JupyterNotebookのipynbファイルを管理するためのアプリ



## 概要

　Jupiter notebookで新しい知識を実践してまとめることが多いが、ipynbファイルの管理が難しい。

　そこでJupiter notebookで作成した勉強用ipynbファイルを管理するアプリを作成する



## 主な機能(実装予定)

- ipynbファイルアップロード
- ipynb→html自動変換機能
- カテゴリ指定機能、カテゴリ検索機能
- 要約文追加機能
- 本文検索機能



## 開発環境構築

```bash
$ pwd
/management-jupyter
$ ls
Dockerfile          README.md           docker-compose.yml  requirements.txt
```

**Dockerfile**

```dockerfile
FROM python:3.8.2

ENV PYTHONUNBUFFERED 1
# デフォルトの locale `C` を `C.UTF-8` に変更する
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# タイムゾーンを日本時間に変更
ENV TZ Asia/Tokyo

# /tmpにappとdockerをコピー
COPY . /tmp

WORKDIR /tmp
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
```

**docker-compose.yml**

```yaml
version: '3'

services:
   jupyter_web:
       build: .
       command: python3 manage.py runserver 0.0.0.0:8000
       volumes:
           - .:/tmp
       ports:
           - "8000:8000"
       tty: true
       depends_on:
           - db
   db:
       image: postgres:10
       ports:
           - "5432"
       environment:
         - POSTGRES_DB=postgres
         - POSTGRES_USER=postgres
         - POSTGRES_PASSWORD=postgres
```

**requirements.txt**

```
beautifulsoup4==4.9.3
jupyter
Django==3.1.2
django-environ
psycopg2>=2.7,<3.0
psycopg2-binary
```



### Djangoプロジェクトの生成

```bash
$ docker-compose run --rm jupyter_web django-admin startproject management_jupyter_project . 
$ ls
Dockerfile                  README.md                   docker-compose.yml          manage.py*                  management_jupyter_project/ requirements.txt
```



### settings.pyの編集

`DATABASES`を以下のように編集

```python 
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'postgres',
       'USER': 'postgres',
       'PASSWORD': 'postgres',
       'HOST': 'db',
       'PORT': 5432,
   }
}
```

言語設定、タイムゾーン設定

```python
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'
```



#### SECRET_KEYはenvironを用いて環境変数化

```python
import environ

env = environ.Env()
env.read_env('.env')

SECRET_KEY = env('KEY')
```



### アプリ生成

```bash
$ docker-compose run --rm jupyter_web django-admin startapp management_jupyter_app
$ docker-compose run --rm jupyter_web python3 manage.py migrate
```





#### アプリ起動

 docker-compose upでローカルサーバーを起動する

#### 初回

```bash
$ docker-compose up --build
```



#### 2回目以降

```bash
$ docker-compose up
```

