from django.shortcuts import render, redirect
from server.apps.insta.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from server.apps.insta.models import User, Post, Comment
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)      
            return render(request, "insta/main.html")
        else:
            return redirect('insta:signup')
    else:
        form = SignupForm()
        context = {
            'form': form,
        }
        return render(request, template_name='insta/signup.html', context=context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('insta:main')
        else:
            context = {
                'form': form,
                'user': user
            }
            return render(request, template_name='insta/login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, template_name='insta/login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect('insta:main')

def main(request):
    user = request.user
    if user.is_authenticated:
        user_name = User.objects.get(username=user)
        posts = Post.objects.order_by('-created_at')
        comments = Comment.objects.all()
        context = {'user': user, 'posts':posts, 'comments':comments}
        liked_users = posts.filter(like_users=user)
        if liked_users.count():
            context['liked_users'] = liked_users
    else:
        context = {'user': user }
    
    return render(request, "insta/main.html", context=context)

def insta_create(request):
    user = request.user
    if request.method == "POST":
        Post.objects.create(
            user = User.objects.get(username=user),
            content = request.POST['content'],
            image = request.FILES.get("image"),
        )
        return redirect("insta:main")
    return render(request, "insta/insta_create.html")

@csrf_exempt
def likes(request, pk):
    user = request.user
    if user.is_authenticated:
        req = json.loads(request.body)
        post_id = req['id']
        btn_type = req['type']
        post = Post.objects.get(id=post_id)
        if btn_type == 'like':
            post.like_users.add(user)
        else:
            post.like_users.remove(user)
            
        post.save()
        return JsonResponse({'id' : post_id, 'type': btn_type})
 
@csrf_exempt
def comment(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    comments = Comment.objects.order_by('created_at')
    context = {'user':user, 'post':post, 'comments':comments,}
    return render(request, "insta/comment.html", context=context)

@csrf_exempt
def comment_create(request, pk):
    user = request.user
    if user.is_authenticated:
        req = json.loads(request.body)
        post_id = req['post_id']
        user = req['user']
        comment = req['comment']
        user_id = User.objects.get(username=user).pk
        Comment.objects.create(
            user = User.objects.get(id=user_id),
            related_post = Post.objects.get(id=post_id),
            content = comment
        )
        comment_id = Comment.objects.last().pk
        return JsonResponse({'post_id' : post_id, 'user': user, 'comment':comment, 'comment_id':comment_id})
    
@csrf_exempt
def comment_delete(request, pk):
    user = request.user
    if user.is_authenticated:
        req = json.loads(request.body)
        post_id = req['post_id']
        comment_id = req['comment_id']
        target_comment = Comment.objects.get(id=comment_id)
        target_comment.delete()
        return JsonResponse({'post_id' : post_id, 'comment_id':comment_id})
