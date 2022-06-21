from django.urls import path
from . import views as posts_views

urlpatterns = [  
    #-- 검색 테스트 위해 임시로 만든 검색 URL --# 
    path('search/', posts_views.search, name='search'),  #posts/search: 검색 폼 -> views.search
    
    path('', posts_views.postList, name='postList'), # posts/: 검색 결과 목록 -> views.postList
    path('<int:postId>/', posts_views.detail, name='detail'), # posts/{postId}: 상세 페이지 -> views.detail
]