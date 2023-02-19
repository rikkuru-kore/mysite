from django.urls import path
from blog.views import (PostListView,
                        PostDetailView,
                        CategoryPostListView,
                        TagPostListView,
                        SearchPostListView,
                        CommentCreateView,
                        ReplyCreateView,
                        CommentDeleteView,
                        ReplyDeleteView
                        )
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',PostListView.as_view(),name='blog-list'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='blog-detail'),
    path("category/<str:slug>/",CategoryPostListView.as_view(),name="category-post-list"),
    path("tag/<str:slug>/",TagPostListView.as_view(),name="tag-post-list"),
    path('search/',SearchPostListView.as_view(),name="search-post-list"),
    path('comment/<int:post_pk>/',CommentCreateView.as_view(),name="comment"),
    path('reply/<int:comment_pk>/',ReplyCreateView.as_view(),name="reply"),
    path('comment/<int:pk>/delete/',CommentDeleteView.as_view(),name="comment-delete"),
    path('reply/<int:pk>/delete/',ReplyDeleteView.as_view(),name="reply-delete"),
    path("login/",LoginView.as_view(template_name="blog/login.html",redirect_authenticated_user=True),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
]
