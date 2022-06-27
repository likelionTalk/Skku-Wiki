from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Report
from django.shortcuts import get_object_or_404, render, redirect

from .models import Post, Report


def postList(request):
    kw = request.POST['kw']  # 검색어
    postList = Post.objects.filter(title__contains=kw)  # 타이틀만 검색함
    # 검색 결과 1개만 존재
    if len(postList) == 1:
        return redirect("posts:detail", str(postList[0].id))

    # 검색 결과 다수 존재
    else:
        for post in postList:
            post.summary = post.body[:len(post.body)] if len(post.body) < 200 else post.body[:200]
        context = {'kw': kw, "length": len(postList), 'postList': postList}
        return render(request, 'search-result-demo.html', context)


def detail(request, postId):
    postDetail = get_object_or_404(Post, pk=postId)
    context = {'postDetail': postDetail}
    return render(request, 'post-detail-demo.html', context)


def report(request, postId):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=postId)
        Report.objects.create(report_body=(request.POST['report_body']), user_id=request.user, post_id=post)
        return redirect("/posts/" + str(postId))
    else:
        post = get_object_or_404(Post, id=postId)
        return render(request, 'post-report.html', {'post': post})


def write(request):
    if request.method == "GET":
        return render(request, 'post-new-demo.html')
    elif request.method == "POST":
        newPost = Post.objects.create(user_id=request.user, title=request.POST['title'], body=request.POST['body'])
        return redirect("/posts/" + str(newPost.id))


def edit(request, postId):
    if request.method == "GET":
        postDetail = get_object_or_404(Post, pk=postId)
        context = {'postDetail': postDetail}
        return render(request, 'post-edit-demo.html', context)
    elif request.method == "POST":
        Post.objects.filter(id=postId).update(title=request.POST['title'])
        Post.objects.filter(id=postId).update(body=request.POST['body'])
        editPost = get_object_or_404(Post, id=postId)
        return redirect("/posts/" + str(editPost.id))


def delete(request, postId):
    deletePost = get_object_or_404(Post, id=postId)
    # if request.user != deletePost.user_id:
    #     messages.error(request, '삭제권한이 없습니다')
    #     return redirect("/posts/" + str(deletePost.id))    
    deletePost.delete()
    return redirect("/")


def like(request, postId):
    return None