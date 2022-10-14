from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)     # auto_now_add = True 는 레코드가 생성될 때 현재 시각이 자동으로 저장
    updated_at = models.DateTimeField(auto_now=True)         # auto_now = True 는 다시 저장할 때 마다 그 시각이 저장

    # author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title}'        # 해당 포스트의 pk 값, 해당 포스트의 title 값

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'