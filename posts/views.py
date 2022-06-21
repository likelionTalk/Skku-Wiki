from django.shortcuts import get_object_or_404, render
from .models import Post

def search(request):
    return render(request, 'search.html')

def postList(request):
    keyWord = request.POST['keyword'] # 검색어
    postList = Post.objects.filter(title__contains=keyWord) # 타이틀만 검색함
    context = {'postList':postList, 'kw':keyWord}
    return render(request, 'result.html', context)

def detail(request, postId):
    postDetail = get_object_or_404(Post, pk=postId)
    context = {'postDetail': postDetail}
    return render(request, 'detail.html', context) 