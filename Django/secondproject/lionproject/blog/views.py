from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm

#all get order_by filter exclude



def home(request):
    blogs = Blog.objects.order_by('-pub_date')
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        blogs = Blog.objects.exclude(writer=author).order_by('-pub_date')
        return render(request, 'home.html', {'blogs':blogs})
    
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request,'home.html',{'blogs':blogs})


def detail(request, id): #블로그에 id값을 통해서 받는다.
    blog = get_object_or_404(Blog, pk = id)
    return render(request,'detail.html',{'blog':blog})

def new(request):
    form = BlogForm()
    return render(request,'new.html', {'form':form})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False) #임시저장
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect('home')

    
def edit(request, id):
    edit_blog = Blog.objects.get(id= id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id): #id받는 이유: 수정해야할 id값을 받아야함
    update_blog = Blog.objects.get(id = id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save() #까먹으면 저장 안됨
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')
