from django.urls import path
from . import views as posts_views

app_name = "posts"   

urlpatterns = [  

    path('', posts_views.home, name='home'),  #posts/: 홈 
    path('search/', posts_views.postList, name='postList'), # posts/search/keyword: 검색 결과 목록 -> views.postList
    path('<int:postId>/', posts_views.detail, name='detail'), # posts/{postId}: 상세 페이지 -> views.detail
]

