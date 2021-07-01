Delete는 templates를 따로 만들 필요가 없다.

단지 delete함수를 만들고, detail에 삭제 버튼만 구현해주면 된다.

삭제방법은 간단함 views.py에 함수 걸어주고

url에는 패스 걸어주고, detail안에는 삭제버튼을 달아주고, 다시 메인화면으로 돌아가게끔 하면 된다.

- detail.html

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3edf5582-d01f-4ad4-adc1-3daf7a586a6f/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3edf5582-d01f-4ad4-adc1-3daf7a586a6f/Untitled.png)

- views.html

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ea66bf70-6faf-492a-bc5d-2bfbb9ca7fc0/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ea66bf70-6faf-492a-bc5d-2bfbb9ca7fc0/Untitled.png)

- urls.html

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1f18ea14-c07d-48c0-96fa-701a453e3ebf/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1f18ea14-c07d-48c0-96fa-701a453e3ebf/Untitled.png)

### 실습화면

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1e869aa1-2c2c-41ca-bb77-d35b5b66fd4c/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1e869aa1-2c2c-41ca-bb77-d35b5b66fd4c/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/039abea2-0b13-4dd6-b862-aa076a845271/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/039abea2-0b13-4dd6-b862-aa076a845271/Untitled.png)
