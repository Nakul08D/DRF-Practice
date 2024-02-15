from django.urls import path
from .views import AuthorList, BookList, AuthorDetail, BookDetail

urlpatterns = [
    path('author/',AuthorList.as_view(), name='author-list'),
    path('author/<int:pk>/',AuthorDetail.as_view(), name='detail-list'),
    path('book/', BookList.as_view(), name='author-list'),
    path('book/<int:pk>/', BookDetail.as_view(), name='detail-list'),
    
    
]
