from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from shop.models import Category

def post_list(request, category_slug=None):
    posts = Post.objects.all()
    category = None
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'blog/post/list.html',
                 {'posts': posts,
                 'category': category,
                 'categories': categories})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)

    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создание объекта комментариев
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            # Сохраниение комментариев в базу данных
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/post/detail.html',
                 {'post': post,
                  'comments': comments,
                  'comment_form': comment_form})