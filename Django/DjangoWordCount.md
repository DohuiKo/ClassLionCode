정보입력하면 반갑습니다! 고도희님! 이렇게 나오도록함.

개발할때는 프론트 백앤드 두파트 나눔. 장고는 조금 더 세분화하도록 함 이러한 디자인 패턴을 MTV패턴이라고 함. templates는 사용자가 실제로 보는 부분이고 Model는 데이터베이스. View는 MTV중에서 핵심이 되는 데이터 처리하는 곳.

이번 실습부터 드디어 여러분들은 에러를 만나게 되실겁니다. 

왜 에러가 날까요? 대부분은 오타! 저장안함!이 원일일 겁니다.

App이란 무엇일까요?

장고 프로젝트를 이루는 작은 단위입니다.

네이버라는 거대한 플랫폼은 하나의 플랫폼 거기에 다양한 서비스가 있음

각 서비스는 페이지가 따로따로 정리. 그리고 이 페이지를 개발 유지 보수한다면 머리가 복잡함.

서비스가 너무 많은데 어떡하지?

장고의 앱은 각각의 서비스별로 분류. 첫번째는 검색전용 메일전용 나눔. 앱은이렇게 하나의 장고 프로젝트를 쪼개서 있음. 규모가 작으면 하나로 해도 충분하지만 대형 포털의 경우 그렇지 않음. 프로젝트 단위로 작업을 함.

app은 [manage.py](http://manage.py) 파일을 이용해서 만든다.

웹사이트는 어떻게 구동되는가?

1. 사용자가 서버에 요청
2. 서버의 view는 model에게 요청에 필요한 데이터를 받음
3. view는 받은 데이터를 적절하게 처리해서 template으로 넘김
4. template은 받은 정보를 사용자에게 보여줌

[[Django 입문] 프로젝트 및 앱 생성, 가상환경 설정](https://developer-alle.tistory.com/331)

가상환경 

- 가상환경 생성. python -m venv 가상환경명

-source 가상환경명/Scripts/activate 입력해서 가상환경 실행

-pip install django: 장고 설치 (pip version 21.1.1)

-장고 프로젝트를 만드는 명령어는 ? django-admin startproject 프로젝트명

-만든 프로젝트에 있는 manage파일은 만들어진 프로젝트의 server를 실행시키기 위한 것

-manage파일의 server실행 : python [manage.py](http://manage.py) runserver.

- 여기까지하면 django가 무사히 실행된다.

- app 만드는데 필요한 [manage.py](http://manage.py) 파일에서 settings.py에 자신의 app이 있다는걸 등록해주어야함. INSTALLED_APPS. app이름 넣을 때 규칙 'firstapp.apps.FirstappConfig' 넣고 저장(이름.apps.대문자파일이름+Config)
- templates을 만들어야한다. app안에 만든다. templates폴더 안에 필요한 html파일 만듬
- 이때 templates 코드

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bfcd531d-9b29-4c21-9580-c2b1f116e6cf/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bfcd531d-9b29-4c21-9580-c2b1f116e6cf/Untitled.png)

이제 views를 만들어야한다.

welcome이라는 함수를 만들어서 이것을 부르면, welcome.html를 띄우도록 함.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4f1019e1-a919-46c8-9740-fe9aa2f1dbde/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4f1019e1-a919-46c8-9740-fe9aa2f1dbde/Untitled.png)

but 인터넷에서 호출할땐 url로 하기 때문에 남은 작업은 url과 views함수를 연결해야하는 것이 문제 ⇒ 이거는 어디서 하느냐, firstproject파일에서 urls.py에서 함.

⇒ firstapp을 사용할 수 있도록 import해준다(여기에서 문제발생). 아무것도 안적혀있는 url ' ' 없어도 됨. name으로한 세번째 인자 넣어주면 url대신 써줄 수 있는 문구 적기 가능.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/303ea0f4-9ccd-439d-a9e2-b8e9bd3e77df/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/303ea0f4-9ccd-439d-a9e2-b8e9bd3e77df/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/74dd2b75-e202-48ba-9feb-d33fb971b5a5/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/74dd2b75-e202-48ba-9feb-d33fb971b5a5/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/14434df6-419f-4540-bdaf-1ec9794bd68a/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/14434df6-419f-4540-bdaf-1ec9794bd68a/Untitled.png)

이렇게 하면 비로소 실행된다!

127.0.0.1은 서버주소인데, 옆에 아무것도 안적혀 있는 이유는 '  ' 이기때문에 아무것도 없는 것임. (빈공간이라서) views가 입력됐다는 뜻.

그렇담 기존에 작성한 코드보면, 뒤에 admin이 있으므로 서버주소 다음 admin을 입력하면 view가 실행되겠네요?

(→ 127.0.0.1**/admin 입력** → 장고 관리창 나옴)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b7c5679d-08ea-4314-b8ac-245d37ab7988/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b7c5679d-08ea-4314-b8ac-245d37ab7988/Untitled.png)

→ 이는 이 views가 실행됨으로써 나오는 site이다.

이제 남은 것은 input박스에 넣은 이름을 page에 띄우는 것이다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8abc553a-67e4-4384-ada1-85b983c008ff/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8abc553a-67e4-4384-ada1-85b983c008ff/Untitled.png)

→ 나중에 view에서 처리할 데이터를 "이름"에 가져와서 님자를 붙이면 됩니다.

—>이제 views에 새로운 함수를 추가합니다.

→ 참고로 "이름"에 해당하는 것에서 데이터를 제대로 받아오려면 {{}} 중괄호 두개를 사용해서 데이터를 받아야한다. (views파일의 hello함수에 있는 UserName을 받는 것임)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4c96a978-7744-4c0a-a97d-be9c6c9f6aa4/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4c96a978-7744-4c0a-a97d-be9c6c9f6aa4/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d414724d-7959-4da1-bba0-dc0a97e79ad6/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d414724d-7959-4da1-bba0-dc0a97e79ad6/Untitled.png)

- 마지막으로 urls.py에 가서 path를 다시 연결해야함. 참고로 path에서 url주소는 무조건 다르게 해야한다. → 따라서 앞서 사용했던 ' '대신 'hello/'(임의 지정)를 임의로 사용함.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b90ff0f1-cdcc-4bfb-a886-fedc3da6decf/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b90ff0f1-cdcc-4bfb-a886-fedc3da6decf/Untitled.png)

views.hello가 지칭하는 바는 views파일의 hello함수를 실행한다는 말임, 세번째인자인 (name="hello")는 보여지는 이름(?)을 뜻함. 이것을 입력하면 url입력할 필요 없이 세번째 인자 이름을 입력해주면 적절한 함수가 불러짐. 그러니 welcome.html에도 hello를 써주면 됨.(이것을 부르기 위해서) 부연설명하자면,  welcome.html에서 action이 hello를 받아서 웹사이트 동작이 될 것임.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de2d905b-2d82-404f-b499-298499b99339/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de2d905b-2d82-404f-b499-298499b99339/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b95301f2-b58a-408b-bfd1-3a9f9d66c465/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b95301f2-b58a-408b-bfd1-3a9f9d66c465/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8ac0d644-a4ab-4f76-82d6-f2ff0907ddb8/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8ac0d644-a4ab-4f76-82d6-f2ff0907ddb8/Untitled.png)

지금까지 했던 과정 정리

1. APP을 생성
2. Template 제작
3. View 제작
4. URL연결

view와 URL연결을 반복하면 하나의 사이트가 만들어진다.

