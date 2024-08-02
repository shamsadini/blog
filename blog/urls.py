from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_article, name='create_article'),
    path('edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete/<int:article_id>/', views.delete_article, name='delete_article'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile_edit, name='profile_edit'),
]