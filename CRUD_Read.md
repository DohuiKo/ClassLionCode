CRUD란?

Create 생성하다

Read 읽다

Update 수정하다

Delete 삭제하다

데이터 베이스 정보를 CRUD한다고 한다.

기술 구현! 실습 필수

Read.

데이터 테이블 만들고 admin으로 데이터 넣는거까지 했는데,

이거를 웹페이지상에서 볼 수 있도록 해야겠죠.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d324d1e1-3221-427d-8f01-998a87af67e2/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d324d1e1-3221-427d-8f01-998a87af67e2/Untitled.png)

home함수 만든다.

database에서 데이터를 달라,고해서 데이터를 받아야한다.

그래서 models.py에서 데이터를 받아야 한다.

→Blog.object.all()

블로그의 객체들을 싹다 가지고 와라.

그 다음, 그 정보를 render해서 home.html에 응답해주어야겠죠.

views.py에서 함수를 하나 만들어주면

무조건 urls.py에도 함수를 만들어줘야 해요.

메소드는 (.)을 통해서 접근 가능하다.

### Path-converter

-path-converter란? 디테일한 페이지를 나타내는 방법이다.

디테일 페이지는 데이터의 개수만큼 페이지가 하나씩 있어야하고,

그걸 보여줄 수 있어야한다.

그렇게되면 패스도 하나씩 늘어나고 함수도 늘어나게 된다.

패스와 함수가 너무 많으면 복잡하기 때문에 url로 path-converter을 적어주면 id값을 통해 page를 다르게 보여줄 수 있고, 또 views.py에 있는 매개변수로 넘겨줄 수도 있다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/69336ac4-92fd-40a4-9130-d87514334b9c/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/69336ac4-92fd-40a4-9130-d87514334b9c/Untitled.png)

### Primary Key

페이지가 말도 안되는 요청했을 때 html에서 404를 제공함.

이 함수를 통해서 찾을 수 없다는 예외처리를 할 수 있다.

그리고 이 함수는 두 가지 매개변수를 받게 된다.

 하나는 우리가 갖고와야할 테이블, 블로그클래스다.

 그리고 pk를 받는데, pk는 Primary key의 약자다.

Primary key는 데이터베이스에서 row하나하나의 데이터를 식별하기 위한 id값이다.

id값이 pk와 같다고 볼 수 있다.

그래서 아래의 코드는

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/468fb370-7d27-4cdb-a4e5-e34e591a0e0c/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/468fb370-7d27-4cdb-a4e5-e34e591a0e0c/Untitled.png)

"id값이 있는 블로그 데이터를 가져오거나 아니면 404 error를 보여주어라."는 뜻이다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/471f257a-8223-4385-b9d4-e340300b5130/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/471f257a-8223-4385-b9d4-e340300b5130/Untitled.png)

html연결할게 있으면 def(request)통해서 연결하고,

값을 화면에 return해주는 식으로 view와 html을 연결한다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fc0b2046-6ce6-42c5-acd2-7881907aaeda/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fc0b2046-6ce6-42c5-acd2-7881907aaeda/Untitled.png)

path로 지정을 해주던 것을 데이터베이스 id값을 통해서 대신할 수 있다.

기본 문법은 <' '> str은 자료형이고 id는 매개변수의 이름이다.

이러면 데이터베이스 값에 따라서 페이지가 다르게 보이기도 하고, views.py의 매개변수로 들어가기도 한다.

두번째 인자는 detail.html함수 이름이고 세번째 인자는 이름에 접근할 수 있도록 하는 것이다.

### detail페이지에 접근하기

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0aab8c65-3f49-4ea0-afb8-bf896152d1a4/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0aab8c65-3f49-4ea0-afb8-bf896152d1a4/Untitled.png)

 {{%  %}} 통해서 해당 객체에 접근을 해왔고,

detail 페이지로 이동하려면 url 에 요청을 보낸다.

detail페이지를 완성하면 이번 실습 끝!

### 실습 완성화면

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3ded4614-7847-403b-9c81-72ea32100011/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3ded4614-7847-403b-9c81-72ea32100011/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7f28d8dc-0737-4ab9-9613-42a9af7d0a4d/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7f28d8dc-0737-4ab9-9613-42a9af7d0a4d/Untitled.png)

more를 클릭하면 detail의 내용을 보여준다.

- detail코드
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta http-equiv="X-UA-Compatible" content="IE=edge">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Detail</title>

<style>

body{text-align: center;}

</style>

</head>

<body>

<h1>{{blog.title}}</h1>

<div>

작성자:{{blog.writer}}

<br>

날짜:{{blog.pub_date}}

</div>

<hr>

<p>{{blog.body}}</p>

</body>

</html>
- views코드
from django.shortcuts import render, get_object_or_404

from .models import Blog

def home(request):

blogs = Blog.objects.all()

return render(request, 'home.html', {'blogs':blogs})

def detail(request, id): #블로그에 id값을 통해서 받는다.

blog = get_object_or_404(Blog, pk = id)

return render(request,'detail.html',{'blog':blog})
- home코드
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
