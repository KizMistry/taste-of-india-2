from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.Nav.about, name='about'),
    path('meal/', views.PostList.as_view(), name='meal'),
    path('<slug:slug>/', views.MealDetail.as_view(), name='meal_detail'),
    path('like/<slug:slug>', views.MealLike.as_view(), name='meal_like'),
    path('booking_list.html/', views.BookingView.as_view(),
         name='booking_list'),
    path('create_booking.html/', views.BookingCreate.as_view(),
         name='create_booking'),
    path('update_booking/<int:booking_id>', views.BookingUpdate.as_view(),
         name='update_booking'),
    path('delete_booking/<int:booking_id>', views.BookingDelete.as_view(),
         name='delete_booking'),
]
