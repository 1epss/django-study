from django.db import models
import os

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)     # auto_now_add = True 는 레코드가 생성될 때 현재 시각이 자동으로 저장
    updated_at = models.DateTimeField(auto_now=True)         # auto_now = True 는 다시 저장할 때 마다 그 시각이 저장
    # author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title}'        # 해당 포스트의 pk 값, 해당 포스트의 title 값

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
