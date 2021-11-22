from django.urls import path
# blog アプリの全ての ビューをインポートする
from . import views

# post_list という名前の ビュー をルートURLに割り当てています
urlpatterns = [
    path('', views.post_list, name='post_list'),
]