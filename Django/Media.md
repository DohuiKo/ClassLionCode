### Media의 개념

- 이용자가 사진을 업로드하면 업로드한 사진을 웹에 띄우는 기능을 media기능이라고 한다.
- static의 경우 요청한 html파일을 서버가 이미 가지고 있으므로 가져다 주기만 하면 된다.
- media는 사진을 업로드하면 서버에 업로드하겠다고 요청합니다. 사진을 넣어서 보내면 서버는 그것을 저장하고 사용자는 그것을 다시 보겠다고 요청하면 그 정보를 이용자에게 다시 보여줍니다. html을 왔다갔다하면서 보여주는 방식이다. 알고 보면 사진의 url을 보내는 방식이기 때문이다.
- 서버는 어떠한 한 곳에 사진 파일을 가지고 경로를 알려주고 클라이언트가 그 경로를 열람할 수수 있게 한다.

### 수강 노트 && 실습 코드

- 추가된 settings.py코드

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a6c91cd-7a54-4ac1-9781-c127c989f3db/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a6c91cd-7a54-4ac1-9781-c127c989f3db/Untitled.png)

- lionproject에 있는 urls.py에 추가된 코드

    settings와 static을 import 해주고 병렬적으로 더한다.

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/15bd152e-ae64-4d68-8b4b-0b6be0aef973/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/15bd152e-ae64-4d68-8b4b-0b6be0aef973/Untitled.png)

- 추가된 [models.py](http://models.py) 코드 부연설명
    - upload_to는 업로드할 폴더를 지정하는 것이다. settings.py에 MEDIA_URL로 지정해둔 media 폴더 안에 blog 폴더를 만들어서 관리하겠다는 설정이다.
    - 빈간일때 아닐때 설정도 지정해준다. (blank = True, null = True)
    - 그런데 새로운 colum이 추가된다면? 에러가 뜨게 된다.

          (그래서 데이터를 삭제하고 다시한다)

    ```python
    from django.db import models

    class Blog(models.Model):
        title = models.CharField(max_length=200)
        writer = models.CharField(max_length=100)
        pub_date = models.DateTimeField() #날짜와 시간
        body = models.TextField() #본문 글자 수는 제한이 없음
        image = models.ImageField(upload_to = "blog/", blank = True, null = True)

        def __str__(self): #객체 호출됐을 때 blog object라고 나오는데, 이를 제목으로 볼 수 있도록 해야함.
            return self.title

        def summary(self):
            return self.body[:100]
    ```

- 데이터 꼬임을 방지하기 위해서 몇몇 data삭제와 모듈 설치
    - db.split migration안의 init같은 파일 삭제.
    - 이미지를 효율적으로 처리할 수 있는 모듈 설치

    = pillow 장고 공식 문서에 이미지 필드 사용할 때 pillow가 무조건 있어야 한다.

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6da8be4f-af05-4329-91fc-e10e40c753bb/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6da8be4f-af05-4329-91fc-e10e40c753bb/Untitled.png)

    - 설치했다면 Migration해야 한다.

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/36ec404b-b39b-4278-b9ee-75dff02c18bd/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/36ec404b-b39b-4278-b9ee-75dff02c18bd/Untitled.png)

    - Migration을 한다면 Migrate도 해야 한다.

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c16ac216-8286-492a-a301-c91e23fb6c5a/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c16ac216-8286-492a-a301-c91e23fb6c5a/Untitled.png)

- 서버를 동작해보자(admin에서)

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ee66fb40-eba7-473f-9c41-11408c7433e1/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ee66fb40-eba7-473f-9c41-11408c7433e1/Untitled.png)

    데이터가 깔끔하게 삭제됐다!

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e09adc3-d954-47ad-a0fc-7389103c6567/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e09adc3-d954-47ad-a0fc-7389103c6567/Untitled.png)

    admin으로 들어가서 관리해보자.

    관리 시에는 Super User로 로그인하자.

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/89f7b04c-a8f4-4677-8a8f-7de78764b0cc/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/89f7b04c-a8f4-4677-8a8f-7de78764b0cc/Untitled.png)

    db를 지웠었기 때문에 super user를 다시 만들어주었다.

    관리자 계정으로 로그인하자.

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ab917f3-579d-4848-a13c-18893ef571c5/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ab917f3-579d-4848-a13c-18893ef571c5/Untitled.png)

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0145bb60-f06d-4e6f-82ba-a0753f9c13b1/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0145bb60-f06d-4e6f-82ba-a0753f9c13b1/Untitled.png)

    admin패널 통해서 이미지 컬럼이 데이터베이스에 제대로 적용됐음을 확인할 수 있다.

    이제 웹페이지에도 사진을 업로드해보자.

- 본문에 이미지 삽입을 추가하고 동작해보자. (실습 코드)
    - new.html코드
    - view.py코드
    - detail.html코드

- 서버를 동작해보자(사용자 입장에서)

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/659eda92-3ef9-443a-886f-64e8435e8ba0/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/659eda92-3ef9-443a-886f-64e8435e8ba0/Untitled.png)

    이제 이미지를 Write에서 추가할 수 있다!

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e6bd418b-6d47-474d-bdd0-15f4afe546eb/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e6bd418b-6d47-474d-bdd0-15f4afe546eb/Untitled.png)

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b26392ad-a6cb-4d5f-87fd-ea22cda745bc/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b26392ad-a6cb-4d5f-87fd-ea22cda745bc/Untitled.png)
