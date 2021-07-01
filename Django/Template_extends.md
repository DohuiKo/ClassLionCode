![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c0f41db5-600e-4df4-97fe-dcae38adae74/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c0f41db5-600e-4df4-97fe-dcae38adae74/Untitled.png)

이런 네이게이션 바를 달고 싶다?

부트스트랩을 이용해보자!

부트스트랩에서 CSS, JS코드와

Navbar(Components에 있음!)코드를 head에 붙여넣기해서 Navbar를 만든다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/16662579-a3eb-459d-9799-e6111af6d0f8/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/16662579-a3eb-459d-9799-e6111af6d0f8/Untitled.png)

우리가 원하는건 Navbar가 어느 페이지에서나 보이는 것인데

home의 head코드를 고치는 것만으로는 home화면에서나 Navbar가 보이고 다른 화면에서는 보이지 않는다.

그렇다면 당연히 detail.html, edit.html, home.html, new.html에 home화면에 붙어 있는 Navbar코드를 복붙해야될 것이다.

그런데 부트스트랩 다 적용시키려고 생각해보니 일일히  html5를 다 적용시켜야한다.

그러나 장고에서는 코드의 중복을 막기 위해서 템플릿의 상속을 지원하고 있다.

### Template상속이란?

기본적인 테이블들을 사용하면 base.html에 놓고, 나머지 html에 상속시켜주는 것이다.

이렇게 상속 방식을 통해서 base.html코드도 받게 되고 독자적인 태그들도 갖게 된다.

이론으로 설명하기에는 쉽지 않다. 코드로 확인하자!

- 방법 설명

    lionproject에 template라는 폴더를 만들고...

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f8798860-bd36-41dc-a21e-7c80215d4ff9/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f8798860-bd36-41dc-a21e-7c80215d4ff9/Untitled.png)

    -base.html을 만든 뒤

     bootstrap에서 긁어온 네비게이션 바를 붙여 넣었다.

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c1e4ed0d-0ee7-4be8-9597-92384b168d50/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c1e4ed0d-0ee7-4be8-9597-92384b168d50/Untitled.png)

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/84dd1e6a-fc6e-4252-b32b-269a7bce63bf/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/84dd1e6a-fc6e-4252-b32b-269a7bce63bf/Untitled.png)

    base에 썼던거 home, detail, edit, new파일에 모두 {% extends 'base.html' %}, {% block content%}, {% endblock %}을 통해서 상속받을 수 있다.

- base.html

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
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
              <a class="navbar-brand" href="#">Navbar</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
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

- detail.html

    ```html
    {% extends 'base.html'%}

    {% block content %}
    <h1>{{blog.title}}</h1>
    <div>
    작성자:{{blog.writer}}
    <br>
    날짜:{{blog.pub_date}}
    </div>
    <hr>
    <p>{{blog.body}}</p>
    <a href="{% url 'edit' blog.id %}">수정하기</a>
    <a href="{% url 'delete' blog.id %}">삭제하기</a>
    {% endblock %}
    ```

- edit.html

    ```html
    {% extends 'base.html'%}

    {%  block content %}

    <h1>Update Your Blog</h1>

    <form action="{% url 'update' blog.id %}" method="post">
        {%csrf_token%}
        <p>제목: <input type="text" name = "title" value="{{blog.title}}"></p>
        <p>작성자: <input type="text" name = "writer" value ="{{blog.writer}}"></p>
        본문: <textarea name="body" id="" cols="30" rows="10">{{blog.body}}</textarea>
        <button type="submit">submit</button>
    </form>

    {% endblock %}
    ```

- home.html

    ```html
    {% extends 'base.html' %}

    {% block content %}
        <h1>Blog Project</h1>
        <div>
            <a href="{%url 'new'%}">writer blog</a>
        </div>
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

- new.html

    ```html
    {% extends 'base.html'%}

    {%  block content %}

    <h1>Write Your Blog</h1>

    <form action="{% url 'create'%}" method="post">
        {%csrf_token%}
        <p>제목: <input type="text" name = "title"></p>
        <p>작성자: <input type="text" name = "writer"></p>
        본문: <textarea name="body" id="" cols="30" rows="10"></textarea>
        <button type="submit">submit</button>
    </form>

    {% endblock %}
    ```

### URLS PATH를 관리해보자

CRUD만 했는데도 걸려있는 Path가 많다.

이제 여러 기능을 구현하게 된다면 path가 엄청 쌓이게 된다.

그러면 [urls.py](http://urls.py) 파일이 비정상적으로 커지게 되며 가독성이 떨어지게 된다.

그래서 우리는 url.py를 app별로 관리하는 방법을 알아야 한다.

- 방법 설명

    원래는 lionproject에 있는 urls.py만 사용했다가

    blog app에 있는 url은 이 앱 내부에서 urls.py를 사용할 것이다.

    admin과 home을 남겨두고 나머지를 blog쪽으로 옮긴다.

    path blog/를 주가해주고 blog.urls를 include시켜준다.

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b62b4bd0-e535-4653-9cac-dee2fe19c87a/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b62b4bd0-e535-4653-9cac-dee2fe19c87a/Untitled.png)

- lionpjoject에 있는 urls.py

    ```python
    from django.contrib import admin
    from django.urls import path,include
    from blog.views import home

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', home, name="home"),
        path('blog/', include('blog.urls'))
    ]
    ```

- blog에 있는 urls.py

    ```python
    from django.contrib import admin
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
