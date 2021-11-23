from django.urls import path
# blog アプリの全ての ビューをインポートする
from . import views

# post_list という名前の ビュー をルートURLに割り当てています
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]