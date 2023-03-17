from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about.html', views.Nav.about, name='about'),
    path('book.html', views.Nav.book, name='book'),
    path('meal.html', views.PostList.as_view(), name='meal'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
