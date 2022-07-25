from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post
from .forms import PostForm
from django.http import Http404

def home(request):
    posts = Post.objects.all().order_by('-date_added')
    message = ''
    context = {'posts': posts, 'message': message}
    return render(request, "core/home.html", context)

@login_required
def details(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)
    context = {'post': post}
    return render(request, "core/details.html", context)

@permission_required('core.add_post')
def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('core:home')
    context = {'form': form}
    return render(request, 'core/new_post.html', context)

