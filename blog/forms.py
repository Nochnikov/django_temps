from django import forms

from blog.models import Post, Comment


# class CreatePostForm(forms.Form):
#     title = forms.CharField(label='Title')
#     content = forms.CharField(label='Content')

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ['title', 'content', 'author', 'categories']
        fields = ['title', 'content', 'categories']
        # fields = '__all__'
        # exclude = ['created_at']


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'content']
