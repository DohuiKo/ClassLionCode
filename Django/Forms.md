### 정의

Form 태그, 어떠한 입력 공간을 뜻한다.

폼태그안에 인풋태그 넣어서 클라이언트가 데이터베이스에 형식에 맞게끔 정보 보낼 수 있도록 form태그를 만든다. 그것을 장고에서는 forms.py를 통해서 객체지향을 통해서 만들 수 있다.

### 장점

저번 시간에 이미지 넣으려고 작업을 굉장히 많이 했었다.

그러나 form.py를 통해서 만들면 database모델이 변할때마다 하나하나 다 바꾸어주지 않아도 된다.

메소드 통해 유효성 검사도 할 수 있다. 우리가 만든 html로 받은 데이터가 database가 받기에 적합한 정보인지 유효성 검사 하기 위해서는 몇 가지 코드가 필요하긴 한데, forms.py를 이용하면 메소드를 통해서 더 편하게 사용할 수 있다. 아직까진 장고에서 어떠한 입력 공간을 주겠다 그정도만 알아도 된다.

### 실습코드

- froms.py생성

    ```python
    from django import forms
    from django.forms import fields
    from .models import Blog

    class BlogForm(forms.ModelForm):
        class Meta:
            model = Blog
            fields = ['title','writer','body','image']
    ```

- [views.py](http://views.py) 수정

    ```python
    from django.shortcuts import render, redirect, get_object_or_404
    from django.utils import timezone
    from .models import Blog
    from .forms import BlogForm

    def home(request):
        blogs = Blog.objects.all()
        return render(request, 'home.html', {'blogs':blogs})

    def detail(request, id): #블로그에 id값을 통해서 받는다.
        blog = get_object_or_404(Blog, pk = id)
        return render(request,'detail.html',{'blog':blog})

    def new(request):
        form = BlogForm()
        return render(request,'new.html', {'form':form})

    def create(request):
        new_blog = Blog()
        new_blog.title = request.POST['title']
        new_blog.writer = request.POST['writer']
        new_blog.body = request.POST['body']
        new_blog.pub_date = timezone.now()
        new_blog.image = request.FILES['image']
        new_blog.save()
        return redirect('detail', new_blog.id)

        
    def edit(request, id):
        edit_blog = Blog.objects.get(id= id)
        return render(request, 'edit.html', {'blog':edit_blog})

    def update(request, id): #id받는 이유: 수정해야할 id값을 받아야함
        update_blog = Blog.objects.get(id = id)
        update_blog.title = request.POST['title']
        update_blog.writer = request.POST['writer']
        update_blog.body = request.POST['body']
        update_blog.pub_date = timezone.now()
        update_blog.save() #까먹으면 저장 안됨
        return redirect('detail', update_blog.id)

    def delete(request, id):
        delete_blog = Blog.objects.get(id=id)
        delete_blog.delete()
        return redirect('home')
    ```

- new.html수정

    ```html
    {% extends 'base.html'%}

    {%  block content %}

    <h1>Write Your Blog</h1>

    <form action="{% url 'create'%}" method="post" enctype="multipart/form-data">
        {%csrf_token%}
        {{form.as_p}}
        <button type="submit">submit</button>
    </form>

    {% endblock %}
    ```

### 실습 실행

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/eeb4b94a-4888-4cfc-97c2-8361243c9b07/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/eeb4b94a-4888-4cfc-97c2-8361243c9b07/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4afc497c-0e2b-47d4-a5aa-3c55862ab630/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4afc497c-0e2b-47d4-a5aa-3c55862ab630/Untitled.png)

p태그 감싸주면 제대로 정렬됨 (table을 넣을 수도 있다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/45d57a2c-0607-4494-866d-337cb43dfdad/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/45d57a2c-0607-4494-866d-337cb43dfdad/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/42df5d8c-8682-4127-aab5-85bb121968be/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/42df5d8c-8682-4127-aab5-85bb121968be/Untitled.png)
