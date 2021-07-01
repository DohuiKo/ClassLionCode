### 강의 노트

- App만들기

    account앱을 만들고 settings에 app을 연결시킨다.

    account앱 안에 있는 views에 인증관련 함수를 추가시킨다.

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fe6be505-1da7-4216-ba68-7f291bea3db7/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fe6be505-1da7-4216-ba68-7f291bea3db7/Untitled.png)

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e610ac17-3890-4650-86c9-2b84699ddbe9/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e610ac17-3890-4650-86c9-2b84699ddbe9/Untitled.png)

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/86f5b24d-2162-4706-8178-648a4413a0ab/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/86f5b24d-2162-4706-8178-648a4413a0ab/Untitled.png)

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a359e5b0-791f-464d-a710-a8e603613410/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a359e5b0-791f-464d-a710-a8e603613410/Untitled.png)

- 강의 내용 정리

    manage.py있는 경로에서 앱을 하나 만듭시다.

    startapp account

    유저의 회원가입을 만드는 account를 만들었습니다.

    intalled apps에 account라고  써줍니다.

    본격적인 로그인 회원가입 로그아웃 기능을 만들어야하는데요.

    장고에서는 이미 유저라는 모델을 제공해준다고 했었죠.

    개발할 때 유저모델을 그대로 가져다 쓸 수 있으니

    유저 확장하지 않고 로그인 로그아웃을 보여드리겠습니다.

    그러면 우리는 기존에 제공되는 유저모델을 사용할테니

    모델.py는 건들지 않을거고

    views.py에서 form을 이용해봅시다.

    그러려면 장고에서 contrib.auth에...

    어센티케이션이폼이랑 인증폼이랑 유저크리에이션 폼을 import해줍니다.

    def login_view(request):

        form  = AuthenticationForm()

        return render(request, 'login.html', {'form'})

    (views에 적어줄 코드)

### 실습 코드

- views.py(account)

    ```python
    from django.shortcuts import redirect, render
    from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
    from django.contrib.auth import authenticate,login,logout
    # Create your views here.

    def login_view(request):
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request=request, username = username, password =password)
                if user is not None:
                    login(request,user)
                    
                return redirect("home")

        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form':form})

    def logout_view(request):
        logout(request)
        return redirect("home")
    ```

- urls.py(account)

    ```python
    from django.urls import path
    from .views import *

    urlpatterns = [
        path('login/', login_view, name= "login"),
        path('logout/', logout_view, name = "logout"),
    ]
    ```

- models.py(account)

    ```python
    from django.db import models

    # Create your models here.
    ```

- login.html(account)

    ```python
    {% extends 'base.html'%}

    {%  block content %}

    <h1>Login</h1>

    <form action="{% url 'login'%}" method="post">
        {%csrf_token%}
        {{form.as_p}}
        <button type="submit">submit</button>
    </form>

    {% endblock %}
    ```

- views.py(blog)

    ```python
    from django.urls import path
    from blog.views import *

    urlpatterns = [
        path('<str:id>',detail, name="detail"),
        path('new/', new, name="new"),
        path('create/', create, name="create"),
        path('edit/<str:id>', edit, name="edit"), #detail페이지로 연결
        path('update/<str:id>',update, name="update"),
        path('delete/<str:id>',delete, name="delete"),
    ]
    ```

- urls.py(blog)

    ```python
    from django.urls import path
    from blog.views import *

    urlpatterns = [
        path('<str:id>',detail, name="detail"),
        path('new/', new, name="new"),
        path('create/', create, name="create"),
        path('edit/<str:id>', edit, name="edit"), #detail페이지로 연결
        path('update/<str:id>',update, name="update"),
        path('delete/<str:id>',delete, name="delete"),
    ]
    ```

- home.html(blog)

    ```html
    {% extends 'base.html' %}
    {% block content %}

        {% if user.is_authenticated %}
        {{user.username}}
        {% endif %}
        <h1>Blog Project</h1>

        <div>
            {% for blog in blogs%}
                <h3> {{blog.title}} </h3>
                {{blog.id}}
                {{blog.writer}}
                {{blog.summary}} <a href="{% url 'detail' blog.id %}">...more</a>
            <br>
            {% endfor %}

        </div>

    {% endblock %}
    ```

- urls.py(lionproject)

    ```python
    """lionproject URL Configuration

    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/3.2/topics/http/urls/
    Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    """
    from django.contrib import admin
    from django.urls import path,include
    from blog.views import home
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', home, name="home"),
        path('blog/', include('blog.urls')),
        path('account/', include('account.urls')),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    ```

- base.html(lionproject)

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name= "viewport" content="width=device-width, initial-scale=1.0">
        <title>BLOG</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
        <style>
            body{text-align: center;}
        </style>
    </head>

    <body>
        {% load static %}
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
              <a class="navbar-brand" href="{% url 'home'%}">
                <img src="{% static 'User.png'%}" alt="" width="50" height="50">    
              </a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="{% url 'new' %}">Write</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="{% url 'login' %}">Login</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="{% url 'logout' %}">Logout</a>
                  </li>
                  <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Dropdown
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                      <li><a class="dropdown-item" href="#">Action</a></li>
                      <li><a class="dropdown-item" href="#">Another action</a></li>
                      <li><hr class="dropdown-divider"></li>
                      <li><a class="dropdown-item" href="#">Something else here</a></li>
                    </ul>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
                  </li>
                </ul>
                <form class="d-flex">
                  <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                  <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
              </div>
            </div>
          </nav>

          <div class="container">
              {% block content %}
              {% endblock %}
          </div>

    </body>
    </html>
    ```

- settings.py(lionproject)

    ```python
    """
    Django settings for lionproject project.

    Generated by 'django-admin startproject' using Django 3.2.4.

    For more information on this file, see
    https://docs.djangoproject.com/en/3.2/topics/settings/

    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/3.2/ref/settings/
    """

    import os
    from pathlib import Path

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-(&z4dq_cq@b-dm9k60^+vd0kypxjok9zq=p8rpnhc*el4j^b04'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',
        'account',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'lionproject.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['lionproject/templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'lionproject.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = '/static/'

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR,'blog','static') ]

    #현재 static 파일들이 어디에 있는지
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    #static 파일을 어디에 모을 건지.

    MEDIA_ROOT = os.path.join(BASE_DIR,'media')
    # 이용자가 업로드한 파일을 모으는 곳
    MEDIA_URL = '/media/'

    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    ```

### 실습화면

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dfe0d22d-2e88-437b-8078-f45d471591d6/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dfe0d22d-2e88-437b-8078-f45d471591d6/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/631c47a5-8998-4a34-92f5-9bcbd95afc4e/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/631c47a5-8998-4a34-92f5-9bcbd95afc4e/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7d85afe0-7a6e-45f6-a8b4-aa452d1a92bf/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7d85afe0-7a6e-45f6-a8b4-aa452d1a92bf/Untitled.png)

로그인시 나한테만 보이는 정보 등장.

로그인 , 로그아웃 기능 성공적.
