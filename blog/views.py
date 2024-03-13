from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.forms import CreatePostForm, CreateCommentForm
from blog.models import Post, Comment
from django.template import loader


# Create your views here.


def index(request):
    # print(request.GET)
    # print(request.GET.get('name', ''))

    posts = Post.objects.all().order_by('-created_at')

    # template = loader.get_template('blog/index.html')

    context = {
        'posts': posts
    }

    return render(request, 'blog/index.html', context)
    # return HttpResponse(template.render(context, request))


# def index(request):
#     # print(request.GET)
#     # print(request.GET.get('name', ''))
#
#     posts = Post.objects.all().order_by('-created_at')
#
#     response =(f'<ul>'
#                f'{"".join([f"<li>{post.title}</li>" for post in posts])}'
#                f'</ul>')
#
#     return HttpResponse(response)


def detail(request, post_id):
    details = Post.objects.get(id=post_id)

    comments = Post.objects.get(comments__post=post_id)

    if comments is not None:
        pass
    else:
        comments = 'No comments yet'

    context = {
        'details': details,
        'comments': comments
    }

    return render(request, template_name='blog/details.html', context=context)

    # return HttpResponse(f"<h1>id {p.id}, {p.title}</h1>"
    #                     f"<p>{p.content}</p>")


def create_comment(request):

    if request.method == 'POST':
        form = CreateCommentForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = 1
            post.save()
            return redirect('index')
        else:
            return HttpResponse('Unexpected error')

    context = {
        'form': CreateCommentForm()
    }

    return render(request, 'blog/comments.html', context=context)


def new_post(request):
    if request.method == 'POST':
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        #
        # new_post = Post(
        #     title=title,
        #     content=content,
        #     author_id=1
        # )
        # new_post.save()
        form = CreatePostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = 1

            # post.save_m2m()?
            post.save()

            return redirect("index")
        else:
            return HttpResponse('Error creating')

    context = {
        'form': CreatePostForm()
    }

    return render(request, 'blog/create_new_post.html', context=context)

# def posts(request):
#
#     post_id = request.GET.get('id', 1)
#
#     p = Post.objects.get(id=post_id)
#     return HttpResponse(f"<h1>id {p.id}, {p.title}</h1>"
#                         f"<p>{p.content}</p>")
