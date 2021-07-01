### Update에 필요한 두 가지 함수

edit: edit.html을 보여주는 함수

update: 수정한 내용을 데이터베이스에 적용시키는 함수

create와 유사하나, 수정할 데이터의 id값을 받아하는 점이 다른 점이다.

수정할 데이터의 id값은 어떻게 받을까?

detail함수를 만들었을 때 path converter랑 매개변수의 id값을 받았던 것을 기억하는가?

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/68a4faf4-8313-4a09-9864-197e61d0d7f5/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/68a4faf4-8313-4a09-9864-197e61d0d7f5/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7408fc19-479b-425d-a1c9-ff45d07e8dea/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7408fc19-479b-425d-a1c9-ff45d07e8dea/Untitled.png)

그것처럼 path converter를 이용해서 특정 글에 id값을 받고, 그 id값으로 데이터 베이스에 데이터를 가져오라고 요청할 것이다.

### Update Code

- detail.html

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7328ef1d-b5dd-45b7-aba2-f6e921f927cd/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7328ef1d-b5dd-45b7-aba2-f6e921f927cd/Untitled.png)

    ```html
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

    <a href="{% url 'edit' blog.id %}">수정하기</a>

    </body>

    </html>
    ```

- urls.py

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/257204c1-a6a8-4c7e-b912-4bf9dd73a6d0/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/257204c1-a6a8-4c7e-b912-4bf9dd73a6d0/Untitled.png)

- edit.html

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1d5bb2a0-3bd2-4f93-be0b-d7bfe763dda8/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1d5bb2a0-3bd2-4f93-be0b-d7bfe763dda8/Untitled.png)

- views.py

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bd64de18-f565-4171-80b0-bf171151b7fa/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bd64de18-f565-4171-80b0-bf171151b7fa/Untitled.png)

- new.html

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a8f7218-f23e-410f-9525-652dc215b00e/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a8f7218-f23e-410f-9525-652dc215b00e/Untitled.png)

### 실습화면

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df3b58a6-5513-4c77-aba0-9ea270d40816/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df3b58a6-5513-4c77-aba0-9ea270d40816/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3bff82b6-7a03-4a30-9a5a-a2954ba4878f/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3bff82b6-7a03-4a30-9a5a-a2954ba4878f/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/749b571d-ffb5-4305-8b5a-89501246667f/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/749b571d-ffb5-4305-8b5a-89501246667f/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ae2b52db-7a77-4ce8-a445-42642b6add1f/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ae2b52db-7a77-4ce8-a445-42642b6add1f/Untitled.png)
