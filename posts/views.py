from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Report


def search(request):
    return render(request, 'search.html')


def postList(request):
    keyWord = request.POST['keyword']  # 검색어

    postList = Post.objects.filter(title__contains=keyWord)  # 타이틀만 검색함
    context = {'postList': postList, 'kw': keyWord}
    return render(request, 'result.html', context)


def detail(request, postId):
    postDetail = get_object_or_404(Post, pk=postId)
    context = {'postDetail': postDetail}
    return render(request, 'detail.html', context)


def report(request, postId):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=postId)
        Report.objects.create(report_body=(request.POST['report_body']), user_id=request.user, post_id=post)
        return redirect("/posts/" + str(postId))
    else:
        post = get_object_or_404(Post, id=postId)
        return render(request, 'report.html', {'post': post})
