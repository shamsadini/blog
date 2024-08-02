from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserChangeForm, CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(request.user, request.POST)

        if 'change_user_info' in request.POST and user_form.is_valid():
            user_form.save()
            return redirect('profile_edit')
        
        if 'change_password' in request.POST and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in after password change
            return redirect('profile_edit')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)
    
    return render(request, 'blog/profile_edit.html', {
        'user_form': user_form,
        'password_form': password_form,
    })


def home(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'blog/create_article.html', {'form': form})

@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, author=request.user)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/edit_article.html', {'form': form, 'article': article})

@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, author=request.user)
    if request.method == 'POST':
        article.delete()
        return redirect('home')
    return render(request, 'blog/delete_article.html', {'article': article})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def login(request):
    return render(request, 'registration/login.html')  # Django provides its own login form


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.increment_views()  # افزایش تعداد بازدیدها
    recent_articles = Article.objects.all().order_by('-created_at')[:5]  # آخرین ۵ مقاله
    return render(request, 'blog/article_detail.html', {'article': article, 'recent_articles': recent_articles})

def search(request):
    query = request.GET.get('q')
    if query:
        results = Article.objects.filter(title__icontains=query) | Article.objects.filter(content__icontains=query)
    else:
        results = Article.objects.none()
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})