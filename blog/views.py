from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# def favicon_boi(request):
#     return (request,'blog/favicon.jpeg')


def user_profile(request, au):
    post = Post.objects.filter(author__username=au)
    print(post)
    count = 0
    for onePost in post:
        count += 1
    print(count)
    return render(request, 'blog/profile.html', {'postz': post[0], 'post_count': count})


def user_posts(request, au):
    post = Post.objects.filter(author__username=au)
    count = 0
    for onePost in post:
        count += 1
    return render(request, 'blog/posts.html', {'posts': post, 'authr': au, 'count': count})


def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = post[::-1]
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        cmnt = request.POST.get('comment', '')
        com = Comment(cmnt=cmnt, authr=request.user, post_id=post.id)
        com.save()
    view_comments = Comment.objects.filter(post_id=post.id)
    return render(request, 'blog/post_detail.html', {'post': post, 'view': view_comments})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def register(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        # print(name)
        # print(email)
        # print(password)
        try:
            user = User.objects.create_user(name, email, password)
            user.save()
        except:
            name_exists = True
            return render(request, 'blog/register.html', {'name': name_exists})
        registered = True
        name_exists = False
        return render(request, 'blog/register.html', {'name': name_exists, 'registered': registered})

    return render(request, 'blog/register.html')


def log_in(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logged = True
            # Redirect to a success page.
            return render(request, 'blog/login.html', {'logged': logged})
            pass
        else:
            # Return an 'invalid login' error message.
            logged = False
            # Redirect to a success page.
            return render(request, 'blog/login.html', {'logged': logged})
    return render(request, 'blog/login.html')


def log_out(request):
    logout(request)
    logged_out = True
    return render(request, 'blog/login.html', {'logged_out': logged_out})
