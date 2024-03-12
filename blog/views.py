from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post
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



    context = {
        'details': details
    }

    return render(request, template_name='blog/details.html', context=context)

    # return HttpResponse(f"<h1>id {p.id}, {p.title}</h1>"
    #                     f"<p>{p.content}</p>")

# def posts(request):
#
#     post_id = request.GET.get('id', 1)
#
#     p = Post.objects.get(id=post_id)
#     return HttpResponse(f"<h1>id {p.id}, {p.title}</h1>"
#                         f"<p>{p.content}</p>")
