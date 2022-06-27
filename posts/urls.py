from django.urls import path
from . import views as posts_views

app_name = "posts"   

urlpatterns = [  
    path('search/', posts_views.postList, name='postList'), # posts/search: 검색 결과 목록
    path('<int:postId>/', posts_views.detail, name='detail'), # posts/{postId}: 상세 페이지 
    path('<int:postId>/report', posts_views.report, name='report'), #posts/report: 신고 
    path('write/', posts_views.write, name='write'), #posts/write: 글 작성 
    path('<int:postId>/edit', posts_views.edit, name='edit'), #posts/edit: 글 수정 
    path('<int:postId>/delete', posts_views.delete, name='delete'), #posts/delete: 글 삭제 
    path('<int:postId>/like', posts_views.like, name='like'), #posts/like: 글 좋아요
]