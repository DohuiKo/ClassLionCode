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