from django.urls import path
from Userposts import views


urlpatterns = [
    path('',views.PostsListView.as_view(),name='posts_list'),
    path('posts/new/',views.PostsCreateView.as_view(),name='posts_new'),
    path('posts/<int:pk>/',views.PostsDetailView.as_view(),name='posts_detail'),
    path('posts/<int:pk>/remove/',views.PostsDeleteView.as_view(),name='posts_delete'),
    path('posts/<int:pk>/edit/',views.PostsUpdateView.as_view(),name='posts_edit'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]