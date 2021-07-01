정적 파일 vs 동적 파일

### 정적 파일

미리 서버에 저장되어 있는 파일

애플스토어처럼 사진들이 서버에 이미 저장이 되어 있어서 html페이지를 보여달라는 요청을 할 때 그 사진을 보여주는 형식. 정적으로 서버에 가만히 있는 파일을 정적 파일이라고 함.

서버에 저장된 그대로를 서비스해주는 파일

- 종류
    - Static : 개발자가 서버를 개발할 때 미리 넣어놓은 정적 파일.
    - Media: 사용자가 업로드할 수 있는 파일

### 동적 파일

서버의 데이터들이 어느정도 가공된다음 보여지는 파일 (상황에 따라 달라질 수 있음)

누가 request인지 post인지 get인지에 따라서 보여지는게 달라지는 파일

### 실습 코드

- [settings.py](http://setting.py) 다루는 방법
- settings.py
- base.html
- home.html

### 실습 화면

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2ff2d9a0-2882-46d0-945c-5bc711c0501d/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2ff2d9a0-2882-46d0-945c-5bc711c0501d/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3c74dade-b401-4440-a386-f48f033ed9b5/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3c74dade-b401-4440-a386-f48f033ed9b5/Untitled.png)

어디에서나 Navbar를 통해서 Write가 가능하게 되었다.
