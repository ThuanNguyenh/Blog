from django import forms
from .models import Comment
from .models import Post
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit = True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()

    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            'body': forms.Textarea(attrs={'class': 'comment-body', 'rows': 4,}),
        }

class createForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "category", "body", "image", "file"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'titleForm','placeholder': 'Enter the title'}),
            'category': forms.TextInput(attrs={'class': 'categoryForm','placeholder': 'Category'}),
            'body': forms.Textarea(attrs={'class': 'bodyForm','placeholder': 'Enter the content'}),
        }

class editForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', "category",'body', 'image', 'file']
            