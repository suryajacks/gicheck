
from django.urls import path 
from .views import ArticleList , ArticlesDetail

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<int:pk>/', ArticlesDetail.as_view()),
      
]
