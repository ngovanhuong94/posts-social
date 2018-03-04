from django.shortcuts import render
from .forms import PostCreateForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def post_create(request):
	form = None
	if request.method == 'POST':
		form = PostCreateForm(request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.author = request.user
			new_post.save()
			messages.success(request, "You created a post")
		else:
			messages.error(request, "Something went wrong , Please try again")
	else:
		form = PostCreateForm()
	return render(request, 'posts/create.html', {'form': form})	