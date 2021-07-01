### Create에 필요한 함수

- new: new.html보여줌
- create: new.html에서 받은 정보를 데이터베이스에 저장

### GET과 POST

http 유통방식에는 여러가지가 있다.

가장 대표적인 방식이 GET과 POST다.

Wordcount페이지에 무언가를 적으면 적힌 내용 그대로 URL에 보인다.

이 방식은 보안에 굉장히 안좋으므로 데이터를 얻기 위한 요청으로만 쓰고,

데이터를 생성할 때는 무조건 POST형식으로 해야한다.

POST형식은 URL에 데이터가 보이지도 않고, CSRF공격을 방지한다.

- CSRF공격: '사이트 간 요청 위조', 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제 등록 등)를 특정 웹사이트에 요청하게 하는 공격. 서버가 데이터 베이스에 공격자에 의해 수정 삭제를 하는 것.

이를 막기 위해 METHOD POST를 썼을 때

form에서 요청이 보내질 때 token이라는 템플릿 변수를 써야한다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ceb58fa5-0d87-4f32-b483-4990c9a12a42/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ceb58fa5-0d87-4f32-b483-4990c9a12a42/Untitled.png)

token이 같이 보내짐으로써(랜덤한 값) 공격이 아니라는걸 인식해서 공격을 방지한다.

### Create만들기

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b1cbfb93-9355-41f4-ab8b-4835a709fd18/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b1cbfb93-9355-41f4-ab8b-4835a709fd18/Untitled.png)

- home.html

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ec23aab6-0436-4007-844f-bae7cd88324e/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ec23aab6-0436-4007-844f-bae7cd88324e/Untitled.png)

    16째 줄, new와 연결해주는 하이퍼링크

    ```html
    <!DOCTYPE html>

    <html lang="en">

    <head>

    <meta charset="UTF-8">

    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <meta name= "viewport" content="width=device-width, initial-scale=1.0">

    <title>BLOG</title>

    <style>

    body{text-align: center;}

    </style>

    </head>

    <body>

    <h1>Blog Project</h1>

    <div>

    <a href="{%url 'new'%}">writer blog</a>

    </div>

    <div>

    {% for blog in blogs%}

    <h3> {{blog.title}} </h3>

    {{blog.id}}

    {{blog.writer}}

    {{blog.summary}} <a href="{% url 'detail' blog.id %}">...more</a>

    <br>

    {% endfor %}

    </div>

    </body>

    </html>
    ```

- views.py

    ```python
    from django.shortcuts import render, redirect, get_object_or_404

    from django.utils import timezone

    from .models import Blog

    def home(request):

    blogs = Blog.objects.all()

    return render(request, 'home.html', {'blogs':blogs})

    def detail(request, id): #블로그에 id값을 통해서 받는다.

    blog = get_object_or_404(Blog, pk = id)

    return render(request,'detail.html',{'blog':blog})

    def new(request):

    return render(request,'new.html')

    def create(request):

    new_blog = Blog()

    new_blog.title = request.POST['title']

    new_blog.writer = request.POST['writer']

    new_blog.body = request.POST['body']

    new_blog.pub_date = timezone.now()

    new_blog.save()

    return redirect('detail', new_blog.id)
    ```

- new.html

    POST방식으로 글을 쓴다. 토큰을 보내서 POST방식 사용.

    ```html
    <h1>Write Your Blog</h1>

    <form action="{% url 'create'%}" method="post">

    {%csrf_token%}

    <p>제목: <input type="text" name = "title"></p>

    <p>작성자: <input type="text" name = "writer"></p>

    본문: <textarea name="body" id="" cols="30" rows="10"></textarea>

    <button type="submit">submit</button>

    </form>
    ```

- urls.py

    ```python
    from django.contrib import admin

    from django.urls import path

    from blog.views import *

    urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home, name="home"),

    path('<str:id>',detail, name="detail"),

    path('new/', new, name="new"),

    path('create/', create, name="create"),

    ]
    ```

### 실습 화면

writer blog를 쓰면 글을 쓸 수 있고,

글을 쓰면 데이터가 저장되어서 home 화면에 보인다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/259aca12-2ce3-4fcb-b6f4-d23c19930556/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/259aca12-2ce3-4fcb-b6f4-d23c19930556/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/94856eff-0717-49d9-968e-af78bc826e9d/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/94856eff-0717-49d9-968e-af78bc826e9d/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f3b5646d-a9cb-4a4b-bdd9-29107c352048/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f3b5646d-a9cb-4a4b-bdd9-29107c352048/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9db2b1c9-aa49-49d9-8d0b-eac10c629318/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9db2b1c9-aa49-49d9-8d0b-eac10c629318/Untitled.png)
