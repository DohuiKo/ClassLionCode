...

다양한 필드 베이스

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ceedaf17-2fc9-495f-9bf5-9d86ae79a156/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ceedaf17-2fc9-495f-9bf5-9d86ae79a156/Untitled.png)

생성날짜같은걸 넣는 필드도 있고, 정수 - 실수 데이터 저장하는 필드도 있습니다.

필드 종류가 많으니 다 알아볼 필요는 없고 필요한 필드를 찾아서 쓰시는게 좋습니다.

괄호안에 넣는 필드 옵션도 종류가 엄청 많습니다.

그래서 필드 옵션도 가급적 검색을 해서 찾아 보시길 바랍니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4eb439d6-ba10-4ac3-9468-1fa29e7b7e3c/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4eb439d6-ba10-4ac3-9468-1fa29e7b7e3c/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7c34b42f-7793-4c0b-8b7b-af704fd97954/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7c34b42f-7793-4c0b-8b7b-af704fd97954/Untitled.png)

- makemigrations와 migrate는 뭘까?

앱 내의 migration  폴더를 만들어서 [models.py](http://models.py)의 변경사항 저장

migrate는 migration폴더를 실행시켜 데이터베이스에 실제로 적용시키는 명령어.

모델에 변경사항 있으면 

makemigrations를 하고,

그 다음으로 migrate하는 식으로

두가지를 함께 해야함.

- 데이터 베이스 안에서 ID Colum은 왜 안만드나요?

→ 이미 저장돼있습니다. 상속받았기 때문이죠.

→ 그러면 우리가 만든 table은 어디에서 확인할 수 있을까요?

→admin패널에서 확인할 수 있습니다.

장고는 admin 패널을 제공해주므로 다른 프레임워크보다 더 쉽게 마이그레이션한 데이터베이스 테이블들을 확인할 수 있습니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d7a825df-1825-46a1-b666-0afd106c5219/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d7a825df-1825-46a1-b666-0afd106c5219/Untitled.png)

admin에 아무나 들어가서 데이터베이스를 만들 수 있는데,

원래 아무나 만지면 안되는 데이터이기 때문에 super유저를 설정해야합니다.

그래서 관리자 권한 가진 슈퍼 유저를 만들어주어야 합니다.

[super user설정 명령어]

python [manage.py](http://manage.py) createsuperuser

아이디 이메일, 비밀번호를 설정한다.

입력해도 terminal 상에서는 보이지 않는다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e9e48b57-bd23-4feb-8da8-a2f7e3280b9b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e9e48b57-bd23-4feb-8da8-a2f7e3280b9b/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/010e2d16-15c6-4b01-bdb5-3f2ac567864e/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/010e2d16-15c6-4b01-bdb5-3f2ac567864e/Untitled.png)

(지정전. 우리가 등록했던 블로그가 없다)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3f906310-4304-4b79-8bdf-6e33bc7c22de/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3f906310-4304-4b79-8bdf-6e33bc7c22de/Untitled.png)

(지정하는 코드를 삽입한다)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fbbfc5f4-b9dd-428e-bd99-d81a34b02664/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fbbfc5f4-b9dd-428e-bd99-d81a34b02664/Untitled.png)

블로그가 생겼다!

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a6e74815-bdf7-480b-a583-cb39dea8ef0a/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a6e74815-bdf7-480b-a583-cb39dea8ef0a/Untitled.png)

add버튼을 클릭해주면 이런 창이 나온다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0c2cafcb-395f-4baa-aba4-a013eb4fdada/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0c2cafcb-395f-4baa-aba4-a013eb4fdada/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0900fbf7-e0f0-4d99-82f6-4db34988acff/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0900fbf7-e0f0-4d99-82f6-4db34988acff/Untitled.png)

위 코드 활용하면 return값이 글에 쓰였던 제목의 데이터가 되어서

제목 그대로 화면상에 노출이된다.

여기까진 아직 database가 이렇게 돼있다는 것만 확인하는 작업이었다.
