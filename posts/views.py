from django.shortcuts import get_object_or_404, render, redirect
from .models import Post

def home(request):
    return render(request, 'home.html')

def postList(request):
    kw = request.POST['kw'] # 검색어
    postList = Post.objects.filter(title__contains=kw) # 타이틀만 검색함
    # 검색 결과 1개만 존재
    if len(postList) == 1:
        return redirect("posts:detail", str(postList[0].id))
    
    # 검색 결과 다수 존재
    else:
        for post in postList:
            post.summary = post.body[:len(post.body)] if len(post.body) < 200 else post.body[:200]
        context = {'kw':kw, "length": len(postList), 'postList':postList}
        return render(request, 'result.html', context)

def detail(request, postId):
    postDetail = get_object_or_404(Post, pk=postId)
    context = {'postDetail': postDetail}
    return render(request, 'detail.html', context) 