from django.db import models

class Image(models.Model):
    image = models.ImageField(verbose_name='入力画像', upload_to='before_image/')