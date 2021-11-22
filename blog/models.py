from django.conf import settings
from django.db import models
from django.utils import timezone

# models.Model はポストがDjango Modelだという意味で、Djangoが、これはデータベースに保存すべきものだと分かるようにしています。
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 文字数が制限されたテキストを定義するフィールド
    title = models.CharField(max_length=200)
    # これは制限無しの長いテキスト用です。ブログポストのコンテンツに理想的なフィールドでしょ？
    text = models.TextField()
    # 日付と時間のフィールド
    created_date = models.DateTimeField(default=timezone.now)
    # これは他のモデルへのリンク
    published_date = models.DateTimeField(blank=True, null=True)
    
    # メソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title