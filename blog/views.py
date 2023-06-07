from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from blog.forms import CommentForm, createForm, editForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.

class PostListView(ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 6

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context['comment_form'] = CommentForm()
        context['comment_count'] = Comment.objects.filter(post=post).count()
        return context

# comment
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_count = post.comments.count()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'blog/post.html', {'post':post, 'form': form, 'comment_count': comment_count})

# search
def search(request):
    search_data = request.GET.get('search_data', '')

    if search_data:
        qd = Post.objects.filter(title__icontains=search_data)
    else:
        qd = Post.objects.all().order_by("-date")
    return render(request, 'blog/blog.html', {
        'posts': qd,
        'search_data': search_data,
    })

# search manage
def search_manage(request):
    search_data = request.GET.get('search_data')

    if search_data:
        qd = Post.objects.filter(title__icontains=search_data)
    else:
        user = request.user
        qd = Post.objects.filter(author=user).order_by("-date")
    return render(request, 'blog/manage.html', {
        'posts': qd,
        'search_data': search_data,
    })



# create blog
def create(request):
    if request.method == 'POST':
        form = createForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return HttpResponseRedirect('/blog')
    else:
        form = createForm()
    return render(request, 'blog/create.html', {'form': form})

# edit
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = editForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(request.path, pk=post.pk)
    else:
        form = editForm(instance=post)
    return render(request, 'blog/post.html', {'forms': form, 'post': post})

# manage post
def manage_posts(request):
    user = request.user 
    posts = Post.objects.filter(author=user).order_by('-date')
    return render(request, 'blog/manage.html', {'posts': posts})


# delete blog
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user: # kiểm tra người dùng hiện tại có phải là tác giả hay không
        post.delete()
        return HttpResponseRedirect('/blog')


